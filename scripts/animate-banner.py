"""Assemble the Imagegen layers into the README's looping GIF. Requires Pillow."""

import math
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance


root = Path(__file__).resolve().parents[1]
background = Image.open(root / "assets/animation/background.png").convert("RGB")
assert background.width == background.height * 3, "Expected a 3:1 background"

background = background.resize((1200, 400), Image.Resampling.NEAREST)

sheet = Image.open(root / "assets/animation/samoyed-sprites.png").convert("RGBA")
assert abs(sheet.width * 4 - sheet.height * 6) <= 6, "Expected a 6-by-4 sprite grid"
sprites = []
for index in range(24):
    col, row = index % 6, index // 6
    cell = sheet.crop(
        (
            round(col * sheet.width / 6),
            round(row * sheet.height / 4),
            round((col + 1) * sheet.width / 6),
            round((row + 1) * sheet.height / 4),
        )
    )
    # GIF uses binary transparency; drop faint matte pixels at the sprite edges.
    cell.putalpha(cell.getchannel("A").point(lambda value: 255 if value >= 240 else 0))
    assert cell.getbbox(), f"Sprite {index} is empty"
    sprites.append(cell.resize((310, 310), Image.Resampling.NEAREST))

ground = 369
sprite_x = 1046 - sprites[0].getbbox()[2]
assert sprites[13].getbbox()[3] - sprites[13].getbbox()[1] < 0.65 * (
    sprites[0].getbbox()[3] - sprites[0].getbbox()[1]
), "Sleeping dog must lie down, not just close its eyes"
yawn = sum(
    a == 255 and r > 1.4 * g and r > 1.1 * b
    for r, g, b, a in sprites[6].crop((120, 85, 220, 170)).getdata()
)
assert yawn > 30, "Missing pink tongue in the open yawn"
# Keep the rise readable instead of replacing a low silhouette with a tall one.
rise_tops = [ground - (sprite.getbbox()[3] - sprite.getbbox()[1]) for sprite in sprites[16:21]]
assert all(abs(a - b) <= 40 for a, b in zip(rise_tops, rise_tops[1:])), "Missing rise intermediate"

timeline = [(index % 2, 200) for index in range(18)]
timeline[12:14] = [(2, 100), (3, 200), (2, 100)]
timeline += [
    (4, 500),  # Heavy eyelids.
    (5, 250), (6, 650), (7, 350),  # Yawn.
    (8, 180), (9, 150), (10, 100), (11, 120), (12, 250),  # Drop, plop, settle.
    (13, 500),
]
timeline += [((13, 13, 14, 14, 14, 13, 13, 13)[index % 8], 250) for index in range(16)]
timeline += [
    (15, 350), (16, 250), (17, 220), (18, 220), (19, 180),  # Shift weight, lift hips.
    (20, 500), (21, 200), (22, 180),  # Stand, then lower into the original sit.
]
timeline += [(index % 2, 200) for index in range(15)]
timeline += [(0, 150), (0, 100)]
total_duration = sum(duration for _, duration in timeline)
assert total_duration == 16_000

stars = []
for x, y in ((106, 45), (560, 44), (773, 40), (893, 46), (991, 41), (1128, 113)):
    box = (x - 10, y - 10, x + 11, y + 11)
    patch = background.crop(box)
    mask = patch.convert("L").point(lambda value: 255 if value > 55 else 0)
    stars.append((box, patch, mask))

frames = []
elapsed = 0
for pose, duration in timeline:
    # The tiny background motion needs fewer updates than the character poses.
    phase = math.tau * round(32 * elapsed / (total_duration - timeline[-1][1])) / 32
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
    sprite = sprites[pose]
    position = (sprite_x, ground - sprite.getbbox()[3])
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
    duration=[duration for _, duration in timeline],
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
