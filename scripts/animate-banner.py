"""Assemble the Imagegen layers into the README's looping GIF. Requires Pillow."""

import math
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance


root = Path(__file__).resolve().parents[1]
background = Image.open(root / "assets/animation/background.png").convert("RGB")
sheet = Image.open(root / "assets/animation/idle-sprites.png").convert("RGBA")
assert background.width == background.height * 3, "Expected a 3:1 background"
assert abs(sheet.width - sheet.height * 2) <= 2, "Expected a 4-by-2 sprite grid"

background = background.resize((1200, 400), Image.Resampling.NEAREST)
sprites = []
for index in range(8):
    col, row = index % 4, index // 4
    cell = sheet.crop(
        (
            round(col * sheet.width / 4),
            round(row * sheet.height / 2),
            round((col + 1) * sheet.width / 4),
            round((row + 1) * sheet.height / 2),
        )
    )
    # GIF uses binary transparency; drop faint matte pixels at the sprite edges.
    cell.putalpha(cell.getchannel("A").point(lambda value: 255 if value >= 240 else 0))
    assert cell.getbbox(), f"Sprite {index} is empty"
    sprites.append(cell.resize((332, 332), Image.Resampling.NEAREST))

stars = []
for x, y in ((106, 45), (560, 44), (773, 40), (893, 46), (991, 41), (1128, 113)):
    box = (x - 10, y - 10, x + 11, y + 11)
    patch = background.crop(box)
    mask = patch.convert("L").point(lambda value: 255 if value > 55 else 0)
    stars.append((box, patch, mask))

frames = []
cycle = (0, 1, 2, 3, 7, 1, 2, 3)
for index in range(64):
    phase = math.tau * index / 63
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
    pose = cycle[(index * 32 // 63) % len(cycle)]
    if index in (44, 45):
        pose = 4
    elif index == 46:
        pose = 5
    frame.paste(sprites[pose], (784, 69), sprites[pose])
    frames.append(frame)

assert ImageChops.difference(frames[0], frames[-1]).getbbox() is None, "Loop seam"
eyes = (930, 148, 1004, 177)
assert ImageChops.difference(frames[0].crop(eyes), frames[44].crop(eyes)).getbbox(), "Missing blink"
lettering = frames[0].crop((0, 65, 780, 236))
assert all(
    ImageChops.difference(lettering, frame.crop((0, 65, 780, 236))).getbbox() is None
    for frame in frames
), "Lettering must stay stationary"

# One shared palette prevents color flicker between frames.
palette = frames[0].quantize(colors=256, method=Image.Quantize.MEDIANCUT)
frames = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
output = root / "assets/samoyed-banner.gif"
frames[0].save(
    output,
    save_all=True,
    append_images=frames[1:],
    duration=100,
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
    assert duration == 6400, f"Unexpected loop duration: {duration}"
    result.seek(0)
    first = result.convert("RGB")
    result.seek(result.n_frames - 1)
    assert ImageChops.difference(first, result.convert("RGB")).getbbox() is None
assert output.stat().st_size < 3_000_000, "Banner is too large for a quick README load"
print(f"Saved {output.name}: {output.stat().st_size:,} bytes, seamless 6.4-second loop")
