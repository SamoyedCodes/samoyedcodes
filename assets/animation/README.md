# Animated Samoyed banner

The README uses `../samoyed-banner.gif`: a 1200 × 400 GIF that loops every 16 seconds. The puppy idles with a steady head, subtle chest/tail movement and a slow blink; gives a modest yawn; lowers itself into a soft landing; naps for about four seconds; wakes with a short stretch; then stands and sits gently. The extreme bow, pancake landing and standing overshoot are omitted. The timing eases into and out of each action. The meadow sways and the stars twinkle at a lower update rate to keep the file below 3MB. The lettering stays still. The first and last frames match.

Readers with `prefers-reduced-motion: reduce` get the original `../samoyed-banner.png` through the README's `<picture>` element.

The background and animation poses were created with the built-in Imagegen tool using the original banner as the reference. `background.png` is the clean background. The active `gentle-sprites.png` has 24 keyframes in a six-column, four-row grid, covering idle through sleep and recovery with restrained deformation. During idle, the head layer and its placement come from the same neutral drawing. Breathing affects the chest and tail; blinking replaces only the eyelid strip, preventing upward head snaps. The generator extracts complete connected silhouettes into padded cells, so ears and tails can cross the source grid without being clipped or leaking into adjacent frames. The faint alpha matte is quantized to binary transparency when composing the GIF. Every pose shares the same ground baseline. The earlier sprite sheets remain as artwork references; the generator uses only the gentle sheet.

To rebuild, run `python3 scripts/animate-banner.py` from the repository root with Pillow installed. The script checks the grid, a visible yawn tongue, the low sleeping silhouette, fixed idle head pixels, fixed head placement, visible blink, character bounds, stationary lettering, loop seam, decoded GIF duration, and file size. One shared palette prevents color flicker and reserves a pink entry for the yawn. No API calls or credentials are needed to rebuild.

## Gentle revision prompt

Built-in Imagegen created `gentle-sprites.png` from the expressive sheet after the user requested less exaggeration and removal of the upward head snap.

Use case: precise-object-edit. Edit target / character reference: this 6-column by 4-row pixel Samoyed animation sheet. Revise the 24 poses to be MUCH CALMER, with only about one third of the current squash/stretch intensity. Keep the cute white Samoyed, navy collar, pale periwinkle fur shadows, pixel style and same 24-pose order. It should feel like a relaxed real puppy with a touch of cartoon softness, not a rubbery slapstick character. Small believable anticipation, soft settling, gentle sleepy expressions. No dramatic head throws, enormous gape, pancake body, high-rump extreme bow, giant tail swings or big standing overshoot. A modest natural yawn and comfortable short stretch are enough.

CRITICAL FIX FOR OPENING TWITCH: in frames 1, 2 and 3, keep the head, neck, nose, muzzle, ears, collar, head angle, head center, face proportions, feet and camera angle at EXACTLY THE SAME POSITION AND SCALE. Do NOT lift or tilt the head in idle. Copy the same head pixels into frames 1 and 2; only a tiny change to chest fur and tail tip for breathing. Frame 3 is an exact copy of frame 1 except eyelids closed in a slow blink. Nose and mouth stay fixed. The first three drawings are a quiet idle, not a head movement.

Technical: exactly SIX equal SQUARE cells across and FOUR rows, 3:2 canvas. Real alpha transparency, empty background outside the dogs. No labels/grid/text/scenery/shadows outside dog. Each whole dog fully contained with 12px clear margins per cell; no neighboring fragments. Same fixed front/very slight three-quarter camera as reference, approximate physical dog size maintained, ground paws at 90% cell height. Neutral seated dog about 75% cell height. Lying dog low on its paws at same head size, not enlarged to fill its cell. Tail to viewer's left. Clean crisp pixel clusters and opaque fur, no speckles, haze, gradients or painterly noise.

24 frames left-to-right, top-to-bottom:
1. Relaxed neutral SEATED puppy, eyes open, friendly closed smile, head level and looking forward, ears upright naturally.
2. EXACT same seated head/face/ears/neck and feet as 1; only chest fur gently fuller and tail tip nudged 1-2 pixels. Absolutely no head tilt or upward snap.
3. EXACT same pose/head placement as 1 except eyes closed for a slow blink. Nose/muzzle remain at exactly same coordinates.
4. Slightly sleepy eyelids; head remains nearly level, just a small forward nod, relaxed ears.
5. Small yawn anticipation: chin tucks a little and shoulders relax; only 3-5% shortening, no curling into a ball.
6. Yawn starts: mouth opens moderately, eyelids close, head begins a small backward arc.
7. Comfortable natural YAWN: open dark mouth with small pink tongue, eyes closed, neck extends just 5-8%, head tipped back only slightly. No gigantic mouth or long giraffe neck.
8. Yawn closes and head eases forward along the same small arc; ears softly follow.
9. Content sleepy seated pose, head gently lowered, body retains natural proportions.
10. Begins lying down: front elbows bend and chest lowers over planted paws, rump just a little higher.
11. Lowers belly and hindquarters, paws forward, ears relaxed; a clear modest descent.
12. Soft landing on grass: belly down and forepaws forward; fur spreads only 5-8%, no pancake squash, closed content eyes.
13. Small settle after landing, chin lowering toward front paws; no visible bounce.
14. Fully asleep lying down, chin on paws, eyes closed, tail resting beside body.
15. Sleeping inhale: essentially identical to 14 except upper back/chest rises subtly, chin and paws fixed.
16. Waking: both eyes half-open, head gently lifting, ears relaxed without a huge asymmetrical grin.
17. Awake lying pose, head up a little, front paws extend slightly in preparation to get up.
18. Modest short dog stretch: chest slightly low and hindquarters a little raised, natural comfortable curve. No extreme long bow or tail thrust.
19. Releases the short stretch, shoulders lifting, body nearly halfway up.
20. Pushes up through planted forepaws, rear knees unfolding, natural transfer of weight.
21. Standing normally on all FOUR legs, gentle expression, relaxed curled tail, no tall overshoot.
22. Hips lower into a sit, front paws stay planted, head remains steady.
23. Small soft seated settle, chest fur relaxes; only 3% compression, no bounce.
24. Returns to the SAME neutral seated head/face/body as 1.

Preserve personality through subtle eyelids, natural breathing, gentle weight and relaxed expression. Calmer than the supplied sheet, more alive than a rigid model sheet. In particular the idle has ZERO head angle or neck height change. Return only the transparent 6-by-4 sprite sheet.

## Earlier expressive revision prompt

Built-in Imagegen created `expressive-sprites.png` using `samoyed-sprites.png` as the character reference. The user requested classic squash-and-stretch acting, allowing deliberate off-model poses.

Use case: stylized-concept. Asset type: transparent production pixel-art animation sprite sheet, 24 storytelling KEY POSES. Input image 1 is a reference ONLY for the Samoyed puppy's recognizable identity and colors, NOT for stiff model-sheet posture. Create a new six-column by four-row sheet of the same original puppy animated with the charm of classic hand-drawn feature animation: anticipation, strong line of action, squash and stretch, expressive eyes and brows, overlapping ears and tail, moving through arcs, a sense of weight and appealing comic exaggeration. The previous sheet is too stiff and restrained. Make this noticeably more alive, warm, sleepy, floppy and playful.

Keep recognizable fluffy WHITE Samoyed puppy, black nose, soft black eyes, dark navy collar and pale periwinkle fur shadows. Chunky clean pixel art, crisply clustered square pixels, limited colors; do not use the reference's fine noisy/painterly grain. Expressions and silhouettes should be readable when the sprite is only 90 pixels tall. The puppy MAY go off model for the action: stretch the torso and muzzle during yawn, squash the fluff into a wide pancake on landing, let ears and tail lag and flop. Those deliberate shape changes should tell the story. Preserve approximate visual mass, not rigid measurements. Do NOT draw 24 same-sized seated portraits.

Composition and technical output: exactly SIX equal SQUARE cells per row and FOUR rows, overall 3:2 canvas. One whole dog per cell, pose sequence left to right, top to bottom. Actual transparent alpha background with alpha=0 outside the dogs. No scenery, grass, painted shadows, text, sleep letters, grid, labels, numbers, motion trails or extra characters. Clean empty space around each sprite, no haze, specks, fringe, checkerboard or background gradient. Head and body stay within each cell with safe margins. Ground-contact paws around 90% of cell height. Neutral dog about 72% of cell height, leaving room for tall yawn/standing overshoot. Same fixed front/three-quarter camera. Lying poses stay low, rather than being enlarged to fill the cell. Back of body and fluffy tail toward viewer's left, face toward viewer's right/front, matching reference.

POSES (24 total):
1. Neutral appealing seated pose, bright eyes, soft smile, relaxed fluffy tail curled to left.
2. Cheerful idle inhale: round chest lifts, head tilts a little, tail swishes outward with a soft S-curve. Pose has life, not just recolored fur.
3. Happy slow blink with closed curved eyes; chin tilts slightly, ears relaxed, tail comes around after the body.
4. Drowsy: heavy drooping eyelids, head droops to one side, shoulders sag, ears flop slightly.
5. Yawn ANTICIPATION: puppy curls inward and squashes its torso a little, chin tucked, eyelids squeeze shut, little closed-mouth inhale, tail tucks.
6. Yawn opening: chest starts to arch up, neck lengthens, head tips back, mouth opens; ears beginning to lag downward.
7. BIG YAWN STRETCH: comically tall elongated torso and neck, head tipped back, eyes shut, mouth wide in a tall dark oval with clearly PINK tongue, forepaws stretch slightly forward; expressive natural puppy yawn. Maintain cuteness and fluff, not a scream.
8. Yawn FOLLOW-THROUGH: body relaxing but muzzle still open smaller; head and ears follow an arc forward, floppy tail lags behind.
9. Sleepy EXHALE: puppy sags into a round short soft sit, head tilted forward, half-closed eyes, ears low, little content smile.
10. Lie-down ANTICIPATION: shoulders roll forward over planted front paws, rump briefly up, face looking drowsily at the grass, compressing before the drop.
11. DOWNWARD STRETCH: body elongated diagonally forward/down, forelegs folding, head moving toward paws, rear still slightly high, ears and tail trailing upward a little. A short fast transitional drawing.
12. PLOP IMPACT: clearly WIDER and SHORTER pancake of fluffy puppy against the ground, belly and rump down, forepaws forward, cheeks softly squashed, closed eyes, floppy ears spread outward, tail flops sideways. An adorable soft heavy landing, not a perfectly rigid lying portrait.
13. REBOUND: a small rounded recovery from the squash, chin lifting a little, ears/tail settling a beat later. Softness, not a large jump or airborne bounce.
14. Fully asleep: puppy curled comfortably low, chin ON front paws, peaceful CLOSED eyes, tail snug against its body, ears relaxed.
15. Sleep INHALE: same restful position but fluffy belly/back rises subtly with breath, face remains restful on paws. Much quieter than yawn/plop.
16. Waking: head lifts with one eye open and one still sleepy, one ear perked while the other droops. A charming asymmetrical sleepy expression.
17. Ready to stretch: head up, front paws reach farther forward, shoulders low, hindquarters starting to rise, soft sleepy smile.
18. Deep morning PLAY BOW STRETCH: both front paws extended forward on ground, chest LOW near grass, hips HIGH, hind legs straightening, back long curved arc, fluffy tail curling upward; head low between paws, eyes happily shut. This must be a distinct dog stretch, not a seated portrait.
19. Stretch RELEASE: chest lifts and hindquarters relax, spine returning through a gentle curve, ears and tail follow with delay, both eyes opening.
20. Rising: front paws planted, shoulders moving up and forward, rear knees unfolding beneath the body; a soft curved line of action between bow and standing.
21. Standing OVERSHOOT: puppy reaches a little tall and proud on all FOUR paws, neck long, bright face, tail lifted, ears perked. A slight upward stretch, not a jump.
22. Sitting DESCENT: hips tuck under and lower, front legs stay planted, fluffy tail trails outward, head still a little high from standing.
23. Seated SQUASH: rump lands softly, torso short and round, cheeks and chest fluff spread slightly, ears dipping after the body, eyes gently closed. Smaller squash than plop.
24. Settle back into frame 1's neutral seated design, open eyes and warm smile, ears and tail catching up.

Make the story emotionally readable and fluid through strong expressive drawings. Exaggeration and appealing deformation ARE DESIRED, especially frames 5-9, 11-13, 18 and 21-23. Crisp pixels, clean transparent silhouettes. Return only the 6-by-4 transparent sheet.

### Expressive sheet cleanup prompt

Use case: precise-object-edit. Edit target: this 6-column by 4-row 24-frame expressive Samoyed sprite sheet. Preserve every expressive pose and its ordered role: head tilt, droopy sleepy face, curled yawn anticipation, tall wide-mouth yawn, floppy ears, broad pancake plop, rebound, restful nap, asymmetrical wake, high-rump low-chest play bow, standing overshoot, soft seated squash. Preserve pixel colors, collar, fluff, character identity and the intended squash/stretch exaggeration. Do NOT make the poses rigid or less expressive.
Fix ONLY sheet extraction defects: some tails or tiny white fragments cross the boundaries between equal square cells. Every cell must contain exactly ONE clean complete dog silhouette, with no disconnected pixels or any fragments of neighboring dogs. Each of the 24 cells must have a completely TRANSPARENT safe border at least 10 pixels wide on all four sides. If a tail or tall ear would touch a cell edge, move that WHOLE dog slightly inward or reduce that whole pose slightly to fit; do not crop or amputate the tail, ears or paws. In particular clear tiny white slivers along cell edges around the high-rump/downward stretch and bow frames. Maintain ground baseline alignment and physical size as far as fitting allows; preserve exaggerated shape changes.
Actual alpha 0 transparent canvas outside each dog, including all gaps and safe borders. Opaque crisp pixel dog, no haze/halo, no background/checkerboard, no labels or grid lines. Exactly 6 equal square cells across, 4 rows, same 3:2 canvas dimensions. No new elements. Return only the cleaned transparent expressive sheet.

## Earlier consistent character revision prompt

Built-in Imagegen generated `samoyed-sprites.png` using `sleep-sprites.png` as the identity reference, with real transparent output:

Use case: identity-preserve. Asset type: one production pixel-art Samoyed animation sprite sheet, REAL TRANSPARENT ALPHA background. Input image 1 is reference ONLY for the white puppy's exact identity, palette, collar, fur shapes and established poses. IGNORE its noisy matte completely. Build ONE CONSISTENT character family: the same young fluffy Samoyed in every frame, never alternating between skinny and round bodies or different face shapes. Preserve the cute ivory fur, cool periwinkle shadows, triangular ears, black eyes/nose, friendly muzzle and navy collar with square buckle. It is a pixel-art sprite, not a rendered painting. Hard square pixel clusters, stable fur texture, limited palette, NO fine grain or random scattered pixels.

OUTPUT: exactly TWENTY-FOUR square cells in SIX COLUMNS by FOUR ROWS. Overall canvas aspect ratio 3:2. No labels, numbers, lines, scenery, text or ground shadow. One WHOLE dog per cell, fully within that cell. Clean alpha 0 everywhere outside the silhouette, no haze, aura, checkerboard, speckles, colored fringes or translucent background. Fur opaque. Leave a little transparent margin on all sides.

REGISTRATION: lock the same physical dog scale, head size, muzzle proportions, collar and camera angle in all 24 cells. Ground-contact baseline EXACTLY 90% down EACH cell, never drifting. Neutral seated height 80% of cell. Keep the front paws planted at the same horizontal location for standing/sitting/lying transitions. The dog's hindquarters and fluffy tail extend left. Lying sprites are LOWER in the cell, not enlarged or recentered to fill it. All front-facing or the same very slight three-quarter front. No mirrored dogs. First and last neutral seated frames MUST be identical. Frames 1-4 form a subtle idle with fixed facial geometry (the nose and collar do not shift sideways).

Read LEFT TO RIGHT, TOP TO BOTTOM:
1. Neutral seated puppy, open round eyes, gentle smile. Matches the reference puppy's relaxed seated design.
2. The EXACT same seated pixels except a tiny chest inhale and tail moving 1-2 pixel clusters, face/head/paws fixed.
3. Same seated puppy beginning a blink, eyelids halfway down. Everything except eyelids identical to frame 1.
4. Same seated puppy with both eyes fully closed in a blink, mouth still the same gentle closed smile. Everything except eyelids identical to frame 1.
5. Getting sleepy: heavy half-closed eyes and chin tipped down slightly, shoulders beginning to relax. Same head/body width as frame 1.
6. Yawn beginning: eyes closed, mouth a small vertical oval.
7. Peak yawn: eyes softly squeezed shut, head tipped just slightly back, mouth opens wide with a small clearly PINK tongue. Natural baby dog yawn, not a scream.
8. Yawn ending: mouth closes, eyes stay sleepy, body softly relaxes.
9. Anticipation for lie-down: body leans slightly forward over the FRONT PAWS; front elbows begin bending, rump still high.
10. Lowering: elbows more bent, chest halfway down, rump beginning to lower. Keep paws planted.
11. Just before plop: chest and belly close to ground, rump almost down, head still up. Clear intermediary between frames 10 and 12.
12. Cute soft PLOP landing: belly and hindquarters down, front paws stretched forward, head up, a small squash in the fluffy torso, same-sized head.
13. Settle: body relaxes out of the small squash, chin lowers halfway to front paws, eyes heavy.
14. Fully asleep: chin ON both front paws, eyes peacefully closed, fluffy tail beside body.
15. Sleeping inhale: EXACT same sleeping pixels as frame 14, except a tiny upper-back/chest expansion by one pixel cluster. Chin, face, ears and paws fixed.
16. Wake: still lying, eyes half open, chin just lifting off paws.
17. Awake prone: head lifted, front paws planted below shoulders, body still on ground.
18. FIRST RISE intermediate: chest shifts FORWARD over planted front paws, elbows bent, shoulders begin to lift. Hindquarters remain low. Natural weight transfer, not a seated jump.
19. SECOND RISE intermediate: front legs now almost straight, chest raised, rear knees tucked UNDER the body; hips are halfway lifted. No floating paws; same torso length.
20. THIRD RISE intermediate: hips nearly upright and rear legs extending, shoulders at almost standing height. A small remaining movement to frame 21, not a sudden large rise.
21. Fully standing on all FOUR legs. Clear natural puppy anatomy, head cheerful, curled fluffy tail to left. Same head size as seated and sleeping frames.
22. SITTING DOWN intermediate: front paws stay planted and front legs straight; hind knees bend, hips beginning to lower. Head stays close to the same height.
23. Almost seated: rump nearly touches ground, rear legs folded, front legs still straight, body easing back into frame 1 proportions.
24. EXACT COPY of frame 1 neutral seated pose, for seamless return to idle.

Critical quality goal: readable physical progression, especially frames 17-23. Show chest-forward push, rear knee tuck, hip lift, four-leg stand, then controlled hip lowering; don't replace these steps with arbitrary seated portraits. The same body moves through the entire sequence. Avoid changing fur patterns or head size between drawings. Output only the clean transparent 6-by-4 sheet.

## Earlier background prompt

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
