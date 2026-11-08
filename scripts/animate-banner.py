"""Assemble the Imagegen layers into the README's looping GIF. Requires Pillow."""

import math
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance


root = Path(__file__).resolve().parents[1]
background = Image.open(root / "assets/animation/background.png").convert("RGB")
assert background.width == background.height * 3, "Expected a 3:1 background"

background = background.resize((1200, 400), Image.Resampling.NEAREST)


def load_sprites(filename, rows):
    sheet = Image.open(root / "assets/animation" / filename).convert("RGBA")
    assert abs(sheet.width * rows - sheet.height * 4) <= 4, "Unexpected sprite grid"
    sprites = []
    for index in range(4 * rows):
        col, row = index % 4, index // 4
        cell = sheet.crop(
            (
                round(col * sheet.width / 4),
                round(row * sheet.height / rows),
                round((col + 1) * sheet.width / 4),
                round((row + 1) * sheet.height / rows),
            )
        )
        # GIF uses binary transparency; drop faint matte pixels at the sprite edges.
        cell.putalpha(cell.getchannel("A").point(lambda value: 255 if value >= 240 else 0))
        assert cell.getbbox(), f"{filename}: sprite {index} is empty"
        sprites.append(cell.resize((332, 332), Image.Resampling.NEAREST))
    return sprites


idle = load_sprites("idle-sprites.png", 2)
sleep = load_sprites("sleep-sprites.png", 4)
ground = 69 + idle[0].getbbox()[3]
# Align both sheets at the neutral front paw, then keep every new pose grounded.
sleep_x = 784 + idle[0].getbbox()[2] - sleep[0].getbbox()[2]
assert sleep[9].getbbox()[3] - sleep[9].getbbox()[1] < 0.65 * (
    sleep[0].getbbox()[3] - sleep[0].getbbox()[1]
), "Sleeping dog must lie down, not just close its eyes"
yawn = sum(
    a == 255 and r > 1.4 * g and r > 1.1 * b
    for r, g, b, a in sleep[3].crop((145, 85, 235, 160)).getdata()
)
assert yawn > 30, "Missing pink tongue in the open yawn"

cycle = (0, 1, 2, 3, 7, 1, 2, 3)
timeline = [("idle", cycle[index % 8], 200) for index in range(20)]
timeline[13:15] = [("idle", 4, 200), ("idle", 5, 200)]
timeline += [
    ("sleep", 1, 500),  # Heavy eyelids.
    ("sleep", 2, 250), ("sleep", 3, 700), ("sleep", 4, 350),  # Yawn.
    ("sleep", 5, 150), ("sleep", 6, 150), ("sleep", 7, 150),
    ("sleep", 8, 250), ("sleep", 9, 500),  # Fold paws, plop, chin down.
]
timeline += [("sleep", (9, 9, 10, 10, 10, 9, 9, 9)[index % 8], 250) for index in range(16)]
timeline += [
    ("sleep", 11, 350), ("sleep", 12, 300), ("sleep", 13, 200),
    ("sleep", 14, 550), ("sleep", 15, 300),  # Wake, push up, stand, sit.
]
timeline += [("idle", cycle[index % 8], 200) for index in range(16)]
timeline.append(("idle", 0, 100))
total_duration = sum(duration for _, _, duration in timeline)
assert total_duration == 16_000

stars = []
for x, y in ((106, 45), (560, 44), (773, 40), (893, 46), (991, 41), (1128, 113)):
    box = (x - 10, y - 10, x + 11, y + 11)
    patch = background.crop(box)
    mask = patch.convert("L").point(lambda value: 255 if value > 55 else 0)
    stars.append((box, patch, mask))

frames = []
elapsed = 0
for bank, pose, duration in timeline:
    # The tiny background motion needs fewer updates than the character poses.
    phase = math.tau * round(32 * elapsed / (total_duration - timeline[-1][2])) / 32
    frame = background.copy()
    # Shift the meadow in small pixel steps while keeping the lettering fixed.
    for y in range(236, 400, 4):
        offset = round(2 * math.sin(phase * 2) * math.sin(math.pi * (y - 236) / 164))
        strip = background.crop((0, y, 1200, min(y + 4, 400)))
        frame.paste(ImageChops.offset(strip, offset, 0), (0, y))
    for number, (box, patch, mask) in enumerate(stars):
        brightness = 0.65 + 0.35 * (1 + math.cos(phase + number)) / 2
        twinkle = ImageEnhance.Brightness(patch).enhance(brightness)
        frame.paste(twinkle, box[:2], mask)
    sprite = idle[pose] if bank == "idle" else sleep[pose]
    position = (784, 69) if bank == "idle" else (sleep_x, ground - sprite.getbbox()[3])
    assert position[0] + sprite.getbbox()[0] >= 780, "Dog overlaps the lettering"
    assert position[0] + sprite.getbbox()[2] <= 1200, "Dog leaves the banner"
    frame.paste(sprite, position, sprite)
    frames.append(frame)
    elapsed += duration

assert ImageChops.difference(frames[0], frames[-1]).getbbox() is None, "Loop seam"
eyes = (930, 148, 1004, 177)
assert ImageChops.difference(frames[0].crop(eyes), frames[13].crop(eyes)).getbbox(), "Missing blink"
lettering = frames[0].crop((0, 65, 780, 236))
assert all(
    ImageChops.difference(lettering, frame.crop((0, 65, 780, 236))).getbbox() is None
    for frame in frames
), "Lettering must stay stationary"

# Sample the whole story so the shared palette includes the yawn's pink tongue.
samples = Image.new("RGB", (150, 50 * len(frames)))
for index, frame in enumerate(frames):
    samples.paste(frame.resize((150, 50), Image.Resampling.NEAREST), (0, index * 50))
palette = samples.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
colors = palette.getpalette()
colors[-3:] = (205, 127, 149)  # Preserve the small pink tongue beside dominant golds.
palette.putpalette(colors)
frames = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
output = root / "assets/samoyed-banner.gif"
frames[0].save(
    output,
    save_all=True,
    append_images=frames[1:],
    duration=[duration for _, _, duration in timeline],
    loop=0,
    disposal=1,
    optimize=True,
)

with Image.open(output) as result:
    assert result.size == (1200, 400) and result.n_frames > 20
    assert result.info.get("loop") == 0, "GIF must loop indefinitely"
    duration = 0
    for index in range(result.n_frames):
        result.seek(index)
        duration += result.info["duration"]
    assert duration == total_duration, f"Unexpected loop duration: {duration}"
    result.seek(0)
    first = result.convert("RGB")
    result.seek(result.n_frames - 1)
    assert ImageChops.difference(first, result.convert("RGB")).getbbox() is None
assert output.stat().st_size < 3_000_000, "Banner is too large for a quick README load"
print(f"Saved {output.name}: {output.stat().st_size:,} bytes, seamless 16-second sleep loop")
