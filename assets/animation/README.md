# Animated Samoyed banner

The README uses `../samoyed-banner.gif`: a 1200 × 400 GIF that loops every 16 seconds. The puppy starts with its breathing, tail movement, and blink; gets sleepy and yawns; folds its paws and plops down; naps for 4.5 seconds with gentle breathing; wakes, stands on all four legs, and sits back into the original idle. The meadow sways and the stars twinkle at a lower update rate to keep the file below 3MB. The lettering stays still. The first and last frames match.

Readers with `prefers-reduced-motion: reduce` get the original `../samoyed-banner.png` through the README's `<picture>` element.

The background and animation poses were created with the built-in Imagegen tool using the original banner as the reference. `background.png` is the clean background, and `idle-sprites.png` contains eight poses in a four-column, two-row grid. `sleep-sprites.png` extends the same character with sixteen poses in a four-column, four-row grid. The faint alpha matte is quantized to binary transparency when composing the GIF. Both sheets align at the neutral front paw; sleep poses share a fixed ground baseline.

To rebuild, run `python3 scripts/animate-banner.py` from the repository root with Pillow installed. The script checks both grids, a visible yawn tongue, the low sleeping silhouette, visible blink, character bounds, stationary lettering, loop seam, decoded GIF duration, and file size. One shared palette prevents color flicker and reserves a pink entry for the yawn. No API calls or credentials are needed to rebuild.

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

## Sleep sprite prompt

Use case: identity-preserve. Asset type: production pixel-art animation SPRITE SHEET with actual transparent alpha, meant to extend an existing GitHub banner animation. Input image 1 is a CHARACTER AND PIXEL STYLE REFERENCE: its existing 4-by-2 sheet of the SAME fluffy Samoyed puppy. Generate a NEW square sprite sheet with EXACTLY SIXTEEN equal SQUARE cells in FOUR COLUMNS by FOUR ROWS, ordered left to right, top to bottom. One whole dog in each cell. No text, labels, numbers, grid, scenery, grass or shadows outside the dog. Canvas transparent everywhere outside the sprites, not black, not checkerboard. Preserve the reference puppy's identity closely: fluffy ivory-white fur, pale cool periwinkle shadow clusters, small triangular ears, round black eyes and nose, dark blue collar with square buckle, thick fluffy tail to viewer's left, front-facing or slight three-quarter front view. Exact same proportions and pixel density across the sixteen cells. Match the reference's friendly baby Samoyed, not a generic adult or a different breed. Crisp square pixel clusters, limited palette, no smooth vector or painterly edges.

ANIMATION CONTINUITY IS CRITICAL: fixed camera; same physical head/body size in every pose. The feet/paws/ground contact baseline must be at EXACTLY 88% of EACH cell's height, and whole dog stays inside its own cell with generous transparent margins. Neutral seated dog height about 80% of cell; lying dog keeps the same head size and lies low near the baseline (do NOT enlarge the lying dog to fill the cell). Front chest/head horizontal position stays consistent; tail and hindquarters extend left. No mirrored sprites or cropped ears/feet. All frames opaque within fur and transparent outside, with NO stray pixels, white haze, or cloudy fringe.

Frame order:
1. Original relaxed seated pose matching the reference top-left dog, eyes open, smiling.
2. Same seated pose with heavy half-closed sleepy eyes and head very slightly bowed.
3. Start yawn seated: eyes squeezed shut, mouth beginning to open in a small vertical oval.
4. Peak adorable yawn seated: eyes shut, muzzle and jaw open wide in a clear tall dark mouth with a tiny pink tongue; head tipped slightly back. Anatomical dog yawn, not a scream.
5. Yawn closing: eyes still sleepy, mouth nearly closed, head relaxing down.
6. Begins lying down: both front elbows bend, shoulders dip, rump still raised, paws stay on the same ground baseline.
7. Lowering further: front legs folding forward, belly coming close to ground, head lower but same head scale.
8. Soft cute plop: belly and hindquarters on ground, front paws extended, head still lifted, fluffy tail beside left hip.
9. Settling to sleep: same prone body, head halfway lowering toward both front paws.
10. Fully asleep: lying with chin resting on front paws, both eyes closed, peaceful face. Same scale as earlier frames; ears relaxed.
11. Sleeping inhale: identical to frame 10, only chest/fluffy back a tiny bit fuller, chin remains on paws.
12. Waking: same prone body with chin lifting a little and eyes half open.
13. Head raised awake: lying body, head fully up, front paws planted ready to push up.
14. Pushing up: forelegs straightening, chest raised, hindquarters still low; natural intermediate between prone and standing.
15. Fully STANDING on all FOUR legs, all paws at the common baseline, head lifted and cheerful, same head size and collar; fluffy curled tail to left. Clear standing body, not seated.
16. Returning to the original seated pose: hindquarters lowered, both front legs straight, eyes open, matching frame 1 as closely as possible for a seamless return to the existing idle loop.

This is a coherent keyframe sheet for ONE dog slowly yawning, plopping, napping, waking, standing up, and sitting again; each anatomical intermediate must be distinct and sensible. Preserve all invariants. Output only the transparent 4-by-4 square sprite sheet.

## Sleep sprite cleanup prompt

Use case: precise-object-edit. Edit target: this sixteen-frame 4-by-4 pixel-art Samoyed animation sprite sheet. Keep the exact sixteen dogs, each pose, placement, sizes, pixel art fur, yawning pink mouth in row 1 column 4, closed sleepy eyes in row 3 columns 2 and 3, and standing pose in row 4 column 3. Keep exactly FOUR columns and FOUR rows with equal square cells; do not move any dog, change the grid, redraw the dogs, or alter proportions.

Change ONLY the transparent background and silhouette cleanup. Remove ALL white haze, gray clouds, red/blue/magenta edge artifacts, dots, noise, detached pixels, and specks in the gaps and around the dogs. Each dog should be a single clean connected pixel silhouette, with opaque fur and absolutely no aura or halo. All pixels outside the dogs' actual fur, ears, tails, feet and bodies must be completely transparent, alpha 0. The margins around all sixteen dogs must be completely clear and empty, including the large gaps above the lying-down dogs. Preserve the pixel stair-step edge of each dog's fur, with no dark outlining added. No background, no checkerboard texture, no grid lines, no labels or new elements. Return only the cleaned, genuinely transparent 4-by-4 sprite sheet.
