# Animated Samoyed banner

The README uses `../samoyed-banner.gif`: a 1200 × 400 GIF that loops every 6.4 seconds. The puppy breathes, wags its tail, and blinks once per loop; the meadow sways and the stars twinkle. The lettering stays still. The first and last frames match.

Readers with `prefers-reduced-motion: reduce` get the original `../samoyed-banner.png` through the README's `<picture>` element.

The background and animation poses were created with the built-in Imagegen tool using the original banner as the reference. `background.png` is the clean background, and `idle-sprites.png` contains eight poses in a four-column, two-row grid. The faint alpha matte is quantized to binary transparency when composing the GIF.

To rebuild, run `python3 scripts/animate-banner.py` from the repository root with Pillow installed. The script checks the grid, visible blink, stationary lettering, loop seam, decoded GIF duration, and file size. No API calls or credentials are needed to rebuild.

## Background prompt

Use case: precise-object-edit. Input image 1 is the edit target: the existing SamoyedCodes banner.
Create a clean animation background plate by removing ONLY the white Samoyed puppy and its collar on the right. Fill exactly the space formerly occupied by the dog with matching midnight navy sky, low blue distant hills, and the existing meadow floor, as though the dog had never been there. Keep all nearby daisies, grass, moon, stars, colors, pixel clusters and every other detail in place.
CRITICAL invariants: preserve the original full 3:1 banner framing; preserve both text lines exactly, "SAMOYEDCODES" and "HEY, I'M BEN", including spelling, letter positions, typography and sizes. Keep the image dark, with hard square pixel edges. No new objects, no dog, no silhouette or shadow of the dog, no people. This is a clean background layer for animation, not a redesigned banner.

## Sprite prompt

Use case: stylized-concept. Asset type: production animation sprite sheet, genuine transparent background.
Input image 1 is the reference for the EXACT puppy design, pixel style, palette, and frontal seated pose. Extract and redraw that single fluffy white Samoyed puppy (upright ears, round black eyes, black nose, smiling muzzle, dark blue collar, ivory fur with pale blue/periwinkle shadows). No scenery and no text.
Produce EXACTLY EIGHT animation frames in a perfectly regular FOUR COLUMNS BY TWO ROWS grid. Overall canvas aspect ratio 2:1. All eight equal SQUARE cells. Each cell contains exactly one whole seated puppy with a fluffy tail visible to its left. Keep generous empty transparent margins inside every cell. No grid lines, no outlines around cells, no labels, no numerals.
The same dog stays in EXACTLY the same front-facing seated pose in all eight cells, at EXACTLY the same scale, foot baseline, head center, and camera angle. Do not redesign the face or change the body orientation. This is a subtle idle cycle, not eight unrelated illustrations.
Frame order, left-to-right across the top row, then the bottom row:
1. Relaxed neutral, eyes open, fluffy tail slightly to the left.
2. Gentle inhale, chest only one pixel fuller, eyes open, tail centered.
3. Peak inhale, chest two pixels fuller, eyes open, tail slightly right.
4. Gentle exhale, chest one pixel fuller, eyes open, tail centered.
5. Relaxed neutral with BOTH EYES FULLY CLOSED in a clear blink, tail slightly left.
6. Relaxed neutral with eyes HALF OPEN, tail centered.
7. Relaxed neutral, eyes fully open, fluffy tail slightly right.
8. Relaxed neutral identical to frame 1 except tail centered, so it loops seamlessly.
Pixel art requirements: chunky crisp square pixels, no smooth or vector-like drawing, no fuzzy or painterly edges, no antialiasing or gradients, consistent pixel size and limited palette throughout. Preserve the reference puppy's friendly expression and proportions. Real alpha transparency everywhere outside the sprites; no checkerboard painted into the image.

## Sprite cleanup prompt

Use case: precise-object-edit. Edit this existing 4-by-2 Samoyed animation sprite sheet.
Preserve EXACTLY the eight puppies, their positions, proportions, pixel art colors, and their eight distinct animation poses, especially the closed eyes in frame 5 and half-open eyes in frame 6.
Fix ONLY the sprite silhouettes and background: remove ALL isolated stray specks, white haze, colored fragments and fringe outside each puppy. Each puppy must be one clean connected pixel silhouette with opaque fur and no cloudy aura. Pixels outside the actual puppy's ears, fur, body, paws and tail must be completely transparent. The empty gaps and margins between all eight sprites must be entirely transparent and clean.
Do not remove white fur or change the animation. Do not add anything. Keep a regular FOUR COLUMNS BY TWO ROWS layout, equal square cells, no labels or grid. Final image must have real alpha transparency. Crisp hard pixel edges, no fuzzy antialiasing.
