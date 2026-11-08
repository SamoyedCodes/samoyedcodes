"""Assemble the Imagegen layers into the README's looping GIF. Requires Pillow."""

import math
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance


root = Path(__file__).resolve().parents[1]
background = Image.open(root / "assets/animation/background.png").convert("RGB")
assert background.width == background.height * 3, "Expected a 3:1 background"

background = background.resize((1200, 400), Image.Resampling.NEAREST)

sheet = Image.open(root / "assets/animation/gentle-sprites.png").convert("RGBA")
assert abs(sheet.width * 4 - sheet.height * 6) <= 6, "Expected a 6-by-4 sprite grid"
# Follow whole silhouettes: expressive ears and tails can cross the cell grid.
remaining = sheet.getchannel("A").point(lambda value: 255 if value >= 240 else 0)
poses = {}
cell_width, cell_height = sheet.width / 6, sheet.height / 4
padding = 12
while remaining.getbbox():
    seed = remaining.tobytes().find(b"\xff")
    ImageDraw.floodfill(remaining, (seed % sheet.width, seed // sheet.width), 128)
    mask = remaining.point(lambda value: 255 if value == 128 else 0)
    remaining.paste(0, mask=mask)
    if mask.histogram()[255] <= 128:
        continue
    box = mask.getbbox()
    col = int((box[0] + box[2]) / 2 / cell_width)
    row = int((box[1] + box[3]) / 2 / cell_height)
    index = row * 6 + col
    assert index not in poses, f"Multiple dogs in sprite cell {index}"
    sprite = sheet.crop(box)
    sprite.putalpha(mask.crop(box))
    cell = Image.new("RGBA", (round(cell_width) + 2 * padding, round(cell_height) + 2 * padding))
    offset = (round(box[0] - col * cell_width + padding), round(box[1] - row * cell_height + padding))
    assert offset[0] >= 0 and offset[1] >= 0, "Sprite exceeds its padded cell"
    assert offset[0] + sprite.width <= cell.width and offset[1] + sprite.height <= cell.height
    cell.paste(sprite, offset)
    size = round(cell.width * 310 / cell_width)
    poses[index] = cell.resize((size, size), Image.Resampling.NEAREST)
assert set(poses) == set(range(24)), "Expected 24 complete dog silhouettes"
sprites = [poses[index] for index in range(24)]

# Keep the idle head fixed; only the chest, tail and eyelids change.
head = (0, 0, sprites[0].width, 200)
eyelids = (170, 119, 255, 141)
closed_eyes = sprites[2].crop(eyelids)
for index in (1, 2):
    sprites[index].paste(sprites[0].crop(head), (0, 0))
sprites[2].paste(closed_eyes, eyelids[:2])

ground = 369
sprite_x = max(1046 - sprites[0].getbbox()[2], 780 - min(sprite.getbbox()[0] for sprite in sprites))
idle_y = ground - sprites[0].getbbox()[3]
assert sprites[13].getbbox()[3] - sprites[13].getbbox()[1] < 0.65 * (
    sprites[0].getbbox()[3] - sprites[0].getbbox()[1]
), "Sleeping dog must lie down, not just close its eyes"
yawn = sum(
    a == 255 and r > 1.4 * g and r > 1.1 * b
    for r, g, b, a in sprites[6].crop((120, 85, 220, 170)).getdata()
)
assert yawn > 30, "Missing pink tongue in the open yawn"
timeline = [(0, 600), (1, 240), (0, 400), (2, 160), (0, 500), (1, 300), (0, 800)]
timeline += [
    (3, 650), (4, 250), (5, 250), (6, 500), (7, 320), (8, 650),  # Gentle yawn and exhale.
    (9, 260), (10, 180), (11, 170), (12, 200), (13, 300),  # Lower, land softly, settle.
]
timeline += [(13, 650), (14, 350)] * 4
timeline += [
    (15, 450), (16, 650), (18, 560), (19, 180),  # Wake and take a short stretch.
    (20, 200), (21, 230), (22, 260), (23, 250), (0, 300),  # Stand, sit and relax.
]
timeline += [(1, 220), (0, 550), (2, 120), (0, 600), (1, 220), (0, 380), (0, 100)]
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
    position = (sprite_x, idle_y if pose in (0, 1, 2) else ground - sprite.getbbox()[3])
    assert position[0] + sprite.getbbox()[0] >= 780, "Dog overlaps the lettering"
    assert position[0] + sprite.getbbox()[2] <= 1200, "Dog leaves the banner"
    frame.paste(sprite, position, sprite)
    frames.append(frame)
    elapsed += duration

assert ImageChops.difference(frames[0], frames[-1]).getbbox() is None, "Loop seam"
eyes = (sprite_x + eyelids[0], idle_y + eyelids[1], sprite_x + eyelids[2], idle_y + eyelids[3])
blink_index = next(index for index, (pose, _) in enumerate(timeline) if pose == 2)
assert ImageChops.difference(frames[0].crop(eyes), frames[blink_index].crop(eyes)).getbbox(), "Missing blink"
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
    first = result.convert("RGB")
    # Check the encoded opening too: blinking may change eyelids, never the head.
    head_mask = Image.new("L", result.size)
    head_mask.paste(sprites[0].crop(head).getchannel("A"), (sprite_x, idle_y))
    head_mask.paste(0, eyes)
    black = Image.new("RGB", result.size)
    duration = 0
    for index in range(result.n_frames):
        result.seek(index)
        if duration < 3000:
            delta = ImageChops.difference(first, result.convert("RGB"))
            assert Image.composite(delta, black, head_mask).getbbox() is None, "Opening head twitch"
        duration += result.info["duration"]
    assert duration == total_duration, f"Unexpected loop duration: {duration}"
    result.seek(0)
    first = result.convert("RGB")
    result.seek(result.n_frames - 1)
    assert ImageChops.difference(first, result.convert("RGB")).getbbox() is None
assert output.stat().st_size < 3_000_000, "Banner is too large for a quick README load"
print(f"Saved {output.name}: {output.stat().st_size:,} bytes, seamless 16-second sleep loop")
