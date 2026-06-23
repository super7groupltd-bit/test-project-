#!/usr/bin/env python3
"""
Unknown Origins — Life on Mars 2055
120 Scene Prompts for Higgsfield AI — Nano Banana Pro
Total audio duration: 7m58s (478 seconds)
Rate: 3.08 words per second
Run: python3 higgsfield_batch.py
"""

import json

TOTAL_DURATION = 478  # 7m58s in seconds
SCENES = [
    {
        "line": 1,
        "voiceover": "It is 6am.",
        "scene": "Alarm clock glowing 6:00 AM in darkness",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Close-up of a hand-drawn alarm clock showing 6:00 AM in bold red numbers, electric yellow and orange glow radiating from the clock face, deep dark navy blue background with tiny bright white stars scattered around, wobbly handwritten text BEEP BEEP in yellow above the clock, red arrow pointing to the time, stick figure hand reaching out to hit snooze. Lots of colour. No realistic shading. No 3D. No cinematic lighting. No realistic humans. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 2,
        "voiceover": "Your alarm goes off.",
        "scene": "Alarm blaring with sound waves exploding outward",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Cartoon alarm clock centre frame with enormous wobbly zigzag sound waves blasting outward in electric yellow and hot pink, the clock shaking with motion lines around it, handwritten label ALARM!! with exclamation marks in red, deep purple and dark blue background packed with bright white stars, stick figure in the top corner covering round-head ears with wide dot eyes. Lots of colour. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 3,
        "voiceover": "You open your eyes.",
        "scene": "Two large cartoon eyes snapping open in darkness",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Extreme close-up of two large cartoon eyes opening wide, thick black eyelid lines lifting to reveal bright white eyes with round black dot pupils, vivid electric blue and purple background behind them, tiny bright white stars scattered in the dark space around the eyes, warm yellow glow at the edges, handwritten text eyes open with a small red arrow, dramatic composition filling the full frame. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 4,
        "voiceover": "And the first thing you see is not a ceiling.",
        "scene": "Stick figure in bed looking up expecting a ceiling but something is wrong",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure with round head lying in a simple drawn bed looking upward with wide surprised dot eyes, thought bubble above showing a drawing of a normal house ceiling with a light bulb, wobbly red question mark next to the thought bubble, deep navy blue and purple background, bright white stars around the edges, handwritten label not a ceiling?? in bright yellow with red arrow. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 5,
        "voiceover": "It is a rust red sky through a reinforced dome window.",
        "scene": "Rust red Martian sky viewed through a thick reinforced dome window",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. View from inside a habitat looking out through a thick reinforced dome window with bolts drawn around the frame, outside sky is a vivid rust red-orange colour packed across the entire background, Martian rocks and dust visible below, handwritten label MARS SKY with red arrow pointing outside, stick figure face pressed against the glass with wide dot eyes and open mouth in awe, warm orange and red tones flooding the scene. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 6,
        "voiceover": "You are not on Earth.",
        "scene": "Stick figure on Mars with Earth crossed out in the corner",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure standing on rust red Martian ground, deep dark blue and purple sky above packed with bright white stars, a drawing of a blue-green Earth visible far away in the top corner with a big red X drawn through it, handwritten bold text NOT EARTH in electric yellow in centre frame with wobbly red underline, red arrow pointing to the stick figure, warm orange glow on the ground. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 7,
        "voiceover": "You are 225 million kilometres from everyone you have ever loved.",
        "scene": "Tiny stick figure on Mars with 225 million km shown between it and Earth",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Wide shot of deep dark purple space background packed with bright white stars, tiny stick figure on the left standing on a small orange-red Mars, blue-green Earth on the far right, a long wobbly dotted line between them with bold handwritten text 225 MILLION KM in electric yellow along the line, red arrows at both ends, stick figure has small round head with a sad dot-eye face and a tiny heart shape above it. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 8,
        "voiceover": "And today is just another Tuesday.",
        "scene": "Calendar showing Tuesday with a boring ordinary tick mark",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Hand-drawn calendar pinned to a wall, TUESDAY circled in red with a big wobbly tick mark, stick figure sitting at a simple table below it looking bored with flat dot eyes and a small straight-line mouth, deep purple and blue background with stars peeking through a small window, handwritten text just another Tuesday in warm yellow beside the calendar, orange and red Martian glow outside the window. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 9,
        "voiceover": "This is what daily life on Mars looks like in 2055.",
        "scene": "Bold title card MARS 2055 with colony scene below",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Bold handwritten text MARS 2055 in massive electric yellow letters filling the top half of frame, wobbly red underline beneath it, below showing a simple drawn colony scene with dome structures on rust red ground, stick figures walking around, a silver rocket parked to one side, deep dark blue and purple sky above packed with bright white stars and a distant glowing sun. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 10,
        "voiceover": "And it is nothing like what you imagined.",
        "scene": "Stick figure shocked face comparing imagined Mars vs real Mars",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure centre frame with wide shocked dot eyes and a dropped O-mouth, two thought bubbles from its round head, left bubble shows imagined Mars as a glamorous shiny silver city, right bubble shows the real cramped dark tunnel habitat, handwritten label imagined over left and reality over right with red arrows, vivid purple and deep blue starry background, electric yellows and warm oranges. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 11,
        "voiceover": "Before we get into this — subscribe to Unknown Origins right now.",
        "scene": "Large subscribe button with stick figure pointing urgently at it",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Large hand-drawn red SUBSCRIBE button taking up centre frame with wobbly thick outline, stick figure on right side pointing at it with both arms raised and wide excited dot eyes, handwritten text UNKNOWN ORIGINS in electric yellow above the button, red arrow pointing at button, deep dark purple and navy blue background with scattered bright white stars, bold bright reds yellows and electric blues. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 12,
        "voiceover": "Every week we cover the strangest mysteries of outer space and the deep ocean.",
        "scene": "Split screen space on one side deep ocean on the other with question marks",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Frame split down the middle with a wobbly black line, left side shows deep dark blue and purple space packed with bright white stars planets and a silver rocket, right side shows deep dark teal ocean with glowing jellyfish a submarine and mysterious underwater structures, handwritten label OUTER SPACE on left and DEEP OCEAN on right in electric yellow, red question marks scattered on both sides, stick figure sitting on the dividing line looking in both directions with wide excited eyes. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 13,
        "voiceover": "You do not want to miss what's coming.",
        "scene": "Stick figure diving toward the screen urgently with speed lines",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure rushing toward viewer with arms stretched wide, round head with huge excited dot eyes and a big open smile, speed lines blasting out behind it in electric yellow and vivid orange, handwritten text DON'T MISS THIS in bold red wobbly letters at the top, deep dark purple and blue starry background, bright stars scattered everywhere, composition feels urgent and dynamic. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 14,
        "voiceover": "Let's start with how you got there.",
        "scene": "Rocket launching from Earth heading toward Mars",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Silver rocket with thick uneven outline blasting off from a blue-green Earth at the bottom left, huge orange and yellow flame shooting downward, deep dark purple and navy space background packed with bright white stars, dotted line path arcing toward a small orange Mars in the top right corner, handwritten label HOW YOU GOT THERE with red arrow, stick figure waving from a tiny window in the rocket with wide dot eyes. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 15,
        "voiceover": "Because the journey alone is enough to change you forever.",
        "scene": "Before and after stick figure entering and leaving a rocket — completely changed",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Two versions of the same stick figure side by side, left shows it walking into a rocket door smiling labelled BEFORE in green, right shows it emerging from the rocket with slouched posture and a wavy stressed face labelled AFTER in red, between them a wobbly arrow pointing right, deep dark blue and purple starry background, silver rocket in the centre, handwritten text changes you forever in electric yellow. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 16,
        "voiceover": "The trip from Earth to Mars takes between 7 and 9 months.",
        "scene": "Timeline showing 7 to 9 months of travel between Earth and Mars",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Long horizontal wobbly line spanning the full width of frame, blue-green Earth on the far left, orange Mars on the far right, a silver rocket crawling along the path near the middle, bold handwritten text 7-9 MONTHS above the line in electric yellow with a red arrow underneath, calendar pages flying around showing months passing, deep dark purple and blue starry background, stick figure inside rocket window looking bored. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 17,
        "voiceover": "Nine months in a spacecraft roughly the size of a large house.",
        "scene": "Spacecraft cross-section the size of a house with stick figures inside",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Cross-section cut-through of a silver spacecraft showing its full interior roughly the size of a drawn house, stick figures crammed in at different levels with bunk beds a tiny kitchen and corridors, handwritten label SIZE OF A HOUSE with red arrow showing the full length, deep dark purple and blue space background outside with bright white stars, vivid oranges and yellows inside the ship from warm lighting. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 18,
        "voiceover": "With the same six to eight people.",
        "scene": "Seven stick figures crammed together with name tags in the spacecraft",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Seven stick figures with round heads and dot eyes squeezed tightly together inside a cramped orange-lit spacecraft interior, each one with a small handwritten name tag, handwritten text SAME 6-8 PEOPLE in electric yellow at top with red arrow pointing to the group, some figures smiling some looking awkward, vivid warm orange and yellow interior walls, deep dark blue starry space visible through a tiny porthole window. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 19,
        "voiceover": "Every single day. No fresh air. No open spaces. No privacy.",
        "scene": "Four small panels showing calendar crossed out, no air, no space, no privacy",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Four equal panels in a grid layout, top left shows calendar with EVERY SINGLE DAY crossed off in red, top right shows crossed-out fresh air symbol with stick figure gasping, bottom left shows stick figure trapped in a tiny box labelled NO OPEN SPACES, bottom right shows stick figure with other figures crowding it labelled NO PRIVACY, all in vivid orange and purple with white stars in background gaps, red text labels on each panel. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 20,
        "voiceover": "Psychologists call what happens to astronauts on long missions the third quarter phenomenon.",
        "scene": "A brain diagram showing the Third Quarter Phenomenon label by a scientist",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Large hand-drawn brain in centre frame with thick black outlines, a red dotted line across the middle labelled HALFWAY with red arrow, the right half of the brain coloured grey and labelled TRAPPED in red, stick figure labelled PSYCHOLOGIST in a white coat pointing at the brain with a stick, handwritten text THIRD QUARTER PHENOMENON in electric yellow at the top in bold wobbly letters, vivid purple and dark blue background with bright white stars. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 21,
        "voiceover": "About halfway through the journey your brain stops feeling excited and starts feeling trapped.",
        "scene": "Journey line showing mood shift from excitement to trapped at the halfway point",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Horizontal journey line from left to right, at the start a stick figure jumps with joy arms raised electric yellow glow, at the halfway point the stick figure sits hunched with grey cloud above it drooping dot eyes, handwritten label HALFWAY — BRAIN FEELS TRAPPED in red with arrow, at the end on right Mars is visible as an orange circle, deep dark purple starry background, vivid transition from warm yellows to cold blues across the scene. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 22,
        "voiceover": "Motivation drops. Mood deteriorates. Arguments break out.",
        "scene": "Three stick figures showing dropping motivation, grey mood, and argument",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Three stick figures in a row inside cramped orange spacecraft corridor, first figure slumped with a downward red bar graph above it labelled MOTIVATION DROPS, second figure coloured grey with a deep frown labelled MOOD DETERIORATES in blue, third figure and a fourth arguing with zigzag speech bubbles and angry expressions labelled ARGUMENTS in red, handwritten labels on each with red arrows, bold electric reds oranges and purples throughout. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 23,
        "voiceover": "And you still have months left to go.",
        "scene": "Calendar with most months still uncrossed — so much time remaining",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Large hand-drawn calendar filling the frame, top half of months crossed out in red X marks, bottom half still blank and uncrossed with a red arrow pointing at them, handwritten text STILL MONTHS TO GO in electric yellow with wavy underline, stick figure looking stressed in the corner with hands on its round head, deep dark blue and purple space background with scattered bright white stars, vivid reds and yellows. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 24,
        "voiceover": "By the time you land on Mars you are already a different person than when you left.",
        "scene": "Same stick figure before and after — completely changed by the journey",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Split composition, left side shows blue-green Earth with a happy stick figure waving goodbye bright yellow glow big smile, right side shows rust-red Mars with the same stick figure arriving but visibly different with slouched posture tired dot eyes stubble lines on face, handwritten label SAME PERSON? with a red question mark in the middle, wobbly red arrow connecting the two, deep dark purple and blue starry space between them. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 25,
        "voiceover": "Landing on Mars is not like landing on Earth.",
        "scene": "Earth landing vs Mars landing side by side — completely different",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Split frame, left side shows a spacecraft gently parachuting down to blue-green Earth stick figure inside waving green fields below, right side shows the same spacecraft with a tiny useless parachute barely open above rust-red Mars stick figure inside looking terrified, handwritten label EARTH LANDING vs MARS LANDING with red arrow showing the parachute failing, vivid blues on left vivid oranges and reds on right. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 26,
        "voiceover": "The atmosphere is so thin — just 1% of Earth's — that parachutes barely work.",
        "scene": "Parachute barely open in thin Mars atmosphere with 1% label shown huge",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. A hand-drawn parachute barely half-open above a spacecraft, wispy thin lines around it showing the thin atmosphere, bold handwritten text ATMOSPHERE: 1% in huge red letters with a red arrow, compared to a second parachute fully open labelled EARTH 100% in green on the opposite side, rust red Martian landscape below, pale orange-red sky, stick figure inside spacecraft window looking sweaty and terrified with wide dot eyes. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 27,
        "voiceover": "You hit the surface using rocket braking systems at the last possible second.",
        "scene": "Rocket firing braking thrusters at the last second above Martian surface",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Silver rocket plunging nose-down toward rust red Martian ground, enormous orange and yellow rocket flames blasting downward from the bottom to slow it down, thick speed lines showing the terrifying descent, rust red cratered surface rushing up to meet it, handwritten text ROCKET BRAKING — LAST SECOND in electric yellow with red arrow, stick figure inside visible through tiny window gripping seat with wide frightened dot eyes. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 28,
        "voiceover": "If anything goes wrong there is no rescue mission coming.",
        "scene": "Distress signal going unanswered — no rescue ships in sight",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Smoking spacecraft on Martian surface with a big red X on it, stick figure standing next to it looking up at empty rust-red and dark purple sky sending an SOS signal in wobbly dashes and dots but the signal just disappears into empty space, handwritten text NO RESCUE COMING in bold red at the top, tiny blue Earth visible in the far distance of the sky, deep dark purple space above the thin atmosphere. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 29,
        "voiceover": "The nearest help is at minimum a 7 month journey away.",
        "scene": "Earth shown impossibly far away — 7 months minimum to reach it",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark purple starry space filling the frame, stick figure on rust-red Mars on the left side, blue-green Earth on the far right side barely visible, a dotted line between them with bold handwritten text 7 MONTHS AWAY in huge electric yellow letters, red arrow pointing at the Earth showing how impossibly far help is, a tiny drawn rocket crawling slowly along the dotted line, the vast empty space between them emphasised with lots of empty starry background. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 30,
        "voiceover": "You land. And for the first time you step outside.",
        "scene": "Airlock opening — first boot print on Martian soil",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Airlock door swinging open with dramatic light pouring through, stick figure in a simple space suit with round helmet taking its very first step onto rust-red Martian soil, foot leaving a boot print in the orange dust, handwritten text FIRST STEP with a red arrow pointing at the boot print, vast empty rust-red landscape stretching out ahead, pale orange-pink sky above, electric yellow light from inside the airlock behind the figure. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 31,
        "voiceover": "The sky is not blue.",
        "scene": "Blue crossed out — Mars sky is shockingly not blue",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Sky taking up top two thirds of the frame with warm pink-orange-red tones, a large hand-drawn blue colour swatch in the corner with a massive red X through it, handwritten text NOT BLUE in huge bold red letters across the sky, stick figure below on rust-red ground staring upward with a puzzled tilted head and question marks around it, vivid oranges and warm pinks fill the sky. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 32,
        "voiceover": "It is a pale butterscotch pink during the day.",
        "scene": "Wide Mars landscape with beautiful alien pale pink sky above",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Wide landscape view, the entire upper half of the frame is a gorgeous pale butterscotch pink and warm peach sky, rust-red Martian ground with rocks below, stick figure standing in middle of the landscape gazing upward with wide amazed dot eyes, handwritten label BUTTERSCOTCH PINK written in the sky with a red arrow, small drawn sun white and tiny in the sky, warm peachy yellows and oranges dominating the colour palette. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 33,
        "voiceover": "At sunrise and sunset it turns blue — the exact opposite of Earth.",
        "scene": "Mars sunrise showing electric blue sky — mind blown comparison with Earth",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Mars at sunrise with the horizon glowing vivid electric blue sky, the ground rust-red and orange, a side-by-side comparison, left shows Earth at sunrise with orange-pink sky labelled EARTH SUNRISE in yellow, right shows Mars sunrise with electric blue glow labelled MARS SUNRISE in yellow, red arrows pointing to each, stick figure with mind exploding with zigzag lines and exclamation marks around its round head. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 34,
        "voiceover": "The ground is iron oxide. Rust.",
        "scene": "The word RUST huge and red — iron oxide ground stretching everywhere",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. The single word RUST in enormous rough wobbly hand-drawn letters filling the upper frame in vivid rust red and dark orange with thick black outline, below it a low angle view of the Martian ground showing vivid rust red iron oxide soil and rocks stretching to the horizon, handwritten label IRON OXIDE with a red arrow pointing at the ground, chemistry symbol Fe2O3 in the corner, pale pink-orange sky above, everything saturated in warm rusty reds and oranges. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 35,
        "voiceover": "As far as you can see in every direction.",
        "scene": "Endless rust-red Mars landscape in every direction with arrows pointing outward",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Panoramic wide shot, rust red Martian landscape stretching to the horizon in every direction, rocks and orange dust everywhere, no trees no water no life, pale pink sky above, stick figure centre frame doing a slow 360-degree turn with arms out footprints in a circle around it, handwritten text AS FAR AS YOU CAN SEE in electric yellow across the top, red arrows pointing in all four directions. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 36,
        "voiceover": "No trees. No grass. No water. No sound.",
        "scene": "Four red X panels — trees, grass, water, sound all absent from Mars",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Four quadrants in the frame, each showing something with a massive red X through it, top left a green tree crossed out labelled NO TREES, top right green grass crossed out labelled NO GRASS, bottom left a blue water droplet crossed out labelled NO WATER, bottom right a speaker with sound waves crossed out labelled NO SOUND, all against a barren rust-red Martian landscape background, vivid green and blue symbols contrasting sharply with the red X marks and orange Martian ground. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 37,
        "voiceover": "Mars is almost completely silent.",
        "scene": "Vast empty Mars landscape — the word SILENCE filling the frame",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Wide Martian landscape with the handwritten word SILENCE taking up the top half of the frame in massive pale blue wobbly letters, wispy broken sound wave lines going nowhere, stick figure in centre of empty rust-red landscape looking tiny against the vast surroundings, handwritten text ALMOST COMPLETELY SILENT in yellow, the background emphasising vast empty space, pale pink sky, the colour palette deliberately quiet with cooler blues and muted oranges. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 38,
        "voiceover": "The atmosphere is too thin to carry sound properly.",
        "scene": "Science diagram showing sound failing to travel through thin Mars atmosphere",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Simple hand-drawn science diagram, on one side a stick figure surrounded by dots as molecules packed tightly labelled EARTH ATMOSPHERE in green with clear wavy sound lines travelling through, on the other side a stick figure surrounded by very sparse dots labelled MARS ATMOSPHERE 1% in red with sound lines fading and disappearing after a short distance, vivid purple and dark blue starry background, handwritten red arrow labelled TOO THIN. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 39,
        "voiceover": "A rock slide a kilometre away would be inaudible.",
        "scene": "Massive rockslide one kilometre away — stick figure hears nothing",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Left side of frame shows a dramatic rockslide on a rust-red Mars cliff face with boulders tumbling orange dust cloud and motion lines everywhere labelled 1 KILOMETRE AWAY with red arrow, right side shows the stick figure standing still one hand to its ear totally unaware question marks above its round head zero sound waves reaching it, handwritten INAUDIBLE in red between the two scenes, pale orange sky. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 40,
        "voiceover": "You are standing on the quietest place any human being has ever stood.",
        "scene": "Tiny stick figure alone on Mars labelled the quietest place humans have stood",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Single stick figure standing tiny in the middle of an enormous rust-red Martian plain, the vast landscape stretching to every edge of the frame, pale pink-orange sky above, complete emptiness around the figure, handwritten text curving around the figure reading THE QUIETEST PLACE ANY HUMAN HAS EVER STOOD in electric yellow, a single red star marker on the spot where the figure stands, deep dark purple sky starting at the top edge. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 41,
        "voiceover": "You cannot stay outside for long.",
        "scene": "Countdown timer ticking — urgency to return inside",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure in a simple space suit on rust-red Martian ground, a large hand-drawn timer counting down above its helmet with red numbers ticking, handwritten text CANNOT STAY OUTSIDE LONG in electric yellow with wobbly underline, red arrows pointing at the timer and the figure, the Martian landscape around it showing thin pale orange atmosphere, the timer dial almost at zero, electric reds and yellows creating urgency. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 42,
        "voiceover": "The temperature swings from minus 73 degrees at night to just above zero during the day.",
        "scene": "Dramatic thermometer showing extreme temperature swing from minus 73 to zero",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Large hand-drawn thermometer filling the left side of the frame, the mercury swinging dramatically from deep blue at the bottom labelled NIGHT: -73 degrees C to near the top in orange labelled DAY: 0 degrees C, bold red wobbly arrows showing the enormous swing, handwritten text TEMPERATURE SWINGS at the top in electric yellow, night side of Mars on the left deep black and purple with stars, day side on the right pale orange sky, stick figure shivering on the night side with chattering teeth lines. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 43,
        "voiceover": "The atmosphere is 95% carbon dioxide.",
        "scene": "Pie chart showing 95% CO2 in Mars atmosphere — overwhelming",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Pie chart taking up most of the frame, a huge overwhelming slice labelled CO2 95% in vivid red, a tiny tiny sliver for everything else in blue, handwritten text MARS ATMOSPHERE at the top in electric yellow with red arrow, bold 95% CARBON DIOXIDE below the chart in red wobbly letters, stick figure next to the chart looking horrified with its hand over its mouth, deep dark purple and blue background with stars. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 44,
        "voiceover": "Without your suit you would lose consciousness in seconds and be dead in minutes.",
        "scene": "Three-panel strip — no suit — passes out — dead on Martian ground",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Three-panel strip inside one image, panel 1: stick figure removes helmet with wide nervous eyes labelled NO SUIT, panel 2: figure clutches throat with dizzy spiral eyes labelled SECONDS in red, panel 3: figure flat on ground with X eyes labelled MINUTES in red, red arrows between each panel, frantic electric red and orange energy throughout, rust-red Mars ground, pale orange sky, handwritten DEAD IN MINUTES in huge bold red letters at the top. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 45,
        "voiceover": "Your home is underground.",
        "scene": "Cross-section view of underground Mars habitat carved below the surface",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Cross-section view of Mars, the rust red surface at the top, underground habitat chambers carved below showing warm orange-lit rooms corridors and stick figures moving about inside, the surface above showing thin pale atmosphere, handwritten text YOUR HOME IS UNDERGROUND with a red arrow pointing down into the habitat, the underground sections warmly lit in electric yellows and oranges contrasting with the cold dark surface above. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 46,
        "voiceover": "Or inside pressurised domes on the surface.",
        "scene": "Glowing pressurised domes on the Mars surface lit from inside",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Two large hand-drawn dome structures sitting on rust-red Martian ground, glowing warm yellow and orange light from inside them showing through the dome windows, small stick figures visible moving inside the domes, a connecting tunnel between the two domes, pale pink-orange Mars sky above with bright white stars beginning to appear at the top, handwritten label PRESSURISED DOMES with red arrow, vivid warm interior light contrasting with cold exterior. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 47,
        "voiceover": "Built from materials shipped from Earth and increasingly from Martian rock itself.",
        "scene": "Rocket delivering supplies and stick figures mining Martian rock to build with",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Silver rocket landed on Mars with cargo bay open and crates of materials being unloaded by stick figures, nearby another stick figure chipping Martian rock from the ground with a pickaxe, handwritten labels FROM EARTH with arrow to crates and FROM MARS with arrow to the mined rock, both being used to build a dome structure on the right side, vivid warm oranges on ground deep dark purple space above electric yellows and blues. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 48,
        "voiceover": "By 2055 the colony has roughly 1,000 people.",
        "scene": "1000 stick figures packed across connected Mars habitats",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Wide shot of connected dome modules and underground tunnels filled with tiny stick figures everywhere, hundreds of them packed in, bold handwritten text approximately 1,000 PEOPLE in electric yellow filling the top with red arrow, the colony sprawling across rust-red landscape, different dome sections connected by tubes, the year 2055 handwritten in the corner, vivid warm oranges and yellows inside the habitat contrasting with dark purple and blue outside. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 49,
        "voiceover": "Spread across several connected habitat modules.",
        "scene": "Blueprint overhead map of several connected habitat modules",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Blueprint-style overhead map view of several large connected rectangular habitat modules drawn with wobbly lines like a hand-sketched floor plan, connecting corridors between each module, stick figures represented as tiny dots spread throughout, handwritten label HABITAT MODULE A B C D with red arrows, scale bar drawn below, rust-red Martian ground visible around the complex, deep dark purple sky above, electric blues and yellows in the drawn map. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 50,
        "voiceover": "Each one the size of a large apartment block.",
        "scene": "Mars habitat module compared in size to an Earth apartment block",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Side-by-side comparison: a familiar Earth apartment block on the left drawn tall with many windows and stick figures in each window labelled APARTMENT BLOCK in green, next to it a Mars habitat module of similar size labelled HABITAT MODULE in orange with the same number of stick figures packed inside, a double-headed red arrow between them showing they are the same size, handwritten SAME SIZE with red underline. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 51,
        "voiceover": "Every cubic metre of living space was expensive to build and is expensive to maintain.",
        "scene": "Dollar signs covering every square metre of the habitat interior",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Cross-section of the habitat interior with vivid warm orange walls, every cubic metre of the interior covered with hand-drawn dollar signs and coin symbols in electric yellow, bold handwritten text EVERY METRE — EXPENSIVE in red at the top, a stick figure in a business suit with dollar sign eyes and a sweat drop, red arrows pointing at everything with price tags, cost explosion dominating the scene. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 52,
        "voiceover": "So personal space is tiny.",
        "scene": "Stick figure barely fitting inside its tiny personal space box",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Bold handwritten text PERSONAL SPACE IS TINY in huge electric yellow letters filling the upper frame, below it a stick figure trying to stretch out its arms inside a very small outlined box that is just barely big enough to contain it, the box squeezed in among other identical boxes on either side, warm orange-lit habitat interior, other stick figures in their own tiny boxes on either side. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 53,
        "voiceover": "You have a room roughly the size of a walk-in wardrobe.",
        "scene": "Floor plan of absurdly tiny room barely larger than the stick figure inside",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Top-down floor plan view of an absurdly tiny room barely bigger than the stick figure inside it, a bunk bed a tiny shelf and zero floor space, the figure standing in the one available spot, handwritten label YOUR ROOM with red arrow, size measurement written as WALK-IN WARDROBE with red double-headed arrow showing the tiny width, warm orange walls, the smallness of the space conveyed by how cramped every element is. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 54,
        "voiceover": "That is your home.",
        "scene": "Stick figure in tiny room pointing at it — THAT IS YOUR HOME — emotional",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure standing in the tiny room looking directly at the viewer one arm gesturing at the cramped space around it, handwritten text THAT IS YOUR HOME in large electric yellow letters at the top, a small framed photo on the wall showing the figure's family, the room looking sparse and lonely with single bunk one shelf and minimal items, warm orange walls, a small emotional moment of quiet sadness in the stick figure's drooping dot eyes. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 55,
        "voiceover": "Your day starts with exercise.",
        "scene": "Stick figure on treadmill at the start of each day in cramped habitat",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure running on a simple hand-drawn treadmill inside an orange-lit habitat corridor, motion lines showing its legs moving, a clock on the wall showing early morning, handwritten text DAY STARTS WITH EXERCISE in electric yellow at the top with red arrow, other stick figures stretching and lifting weights visible in the background, vivid warm orange and yellow interior, the exercise equipment squeezed into every available space. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 56,
        "voiceover": "Not because you want to. Because you have to.",
        "scene": "Reluctant stick figure exercising — NOT because it wants to — bold text",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure lifting a heavy weight with a completely flat unenthusiastic expression, a thought bubble showing it imagining lying in bed instead, handwritten text NOT BECAUSE YOU WANT TO in red wobbly letters at the top, below it in even bigger electric yellow letters BECAUSE YOU HAVE TO with a thick wobbly underline, orange habitat walls, the contrast between the reluctant body language and the determined exercise movement. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 57,
        "voiceover": "Mars gravity is 38% of Earth's.",
        "scene": "Gravity comparison — stick figure jumping on Earth vs Mars — 38% shown huge",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Split frame, left side shows blue-green Earth with stick figure jumping normally jump arc shown in dotted line labelled EARTH 100% GRAVITY in green, right side shows rust-red Mars with same stick figure jumping much higher due to low gravity a much taller jump arc labelled MARS 38% GRAVITY in orange, bold handwritten 38% in enormous electric yellow in the centre, red arrows comparing the two arcs. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 58,
        "voiceover": "Your muscles and bones are constantly losing density.",
        "scene": "Bones and muscles visibly shrinking over time — density loss shown",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Two stick figures side by side, left shows a strong figure with thick bold limbs labelled ARRIVAL in green, right shows the same figure with thinner wobbly limbs labelled MONTHS LATER in red, a red downward arrow between them, handwritten text LOSING DENSITY with red arrow pointing at the shrinking limbs, scientific-style bone cross-sections drawn in the corner showing density decrease, deep dark purple background with bright white stars. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 59,
        "voiceover": "Without two hours of exercise every single day you would become physically unable to return to Earth.",
        "scene": "2-hour timer above exhausted stick figure exercising — or never return to Earth",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Large hand-drawn clock showing 2 HOURS in bold red at the top, stick figure on a treadmill below looking exhausted with sweat drops and drooping eyes but still running, handwritten text EVERY SINGLE DAY in electric yellow, below that OR: CAN NEVER RETURN TO EARTH in red with a red arrow pointing at a tiny blue-green Earth drawing in the corner with a wavy X over it, deep dark purple background. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 60,
        "voiceover": "And here is the thing nobody talks about.",
        "scene": "Stick figure leaning in conspiratorially — the secret nobody mentions",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure leaning toward the viewer with a conspiratorial expression, one hand cupped beside its round head, wide secretive dot eyes, speech bubble beside it containing ... and a small exclamation mark, handwritten text THE THING NOBODY TALKS ABOUT in electric yellow with red arrow, dramatic spotlight effect drawn in rough yellow around the figure, deep dark purple and blue starry background. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 61,
        "voiceover": "After enough time on Mars — some scientists believe your body adapts so completely that returning to Earth becomes impossible.",
        "scene": "Fork in the road — path back to Earth blocked — body adapted too fully to Mars",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Fork in the road with stick figure at the split, one path curves toward blue-green Earth but is blocked by a red barrier with X, other path continues toward orange Mars, handwritten text BODY ADAPTS COMPLETELY in electric yellow at top, red arrow pointing at the Earth path with IMPOSSIBLE written beside the barrier, scientists drawn as stick figures in white coats beside the scene with clipboards wide eyes showing disbelief, deep dark purple and blue starry space background. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 62,
        "voiceover": "The gravity would crush you. Your heart wouldn't cope.",
        "scene": "Earth gravity crushing a Martian stick figure — heart shown struggling",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Left side: stick figure on Earth being squashed by huge downward arrows representing gravity the figure's legs buckling and compression lines around its body labelled GRAVITY WOULD CRUSH YOU in massive red letters. Right side: large hand-drawn heart with a worried sweating face and a falling bar graph below it labelled YOUR HEART WOULDN'T COPE in red. Both sides against vivid blue Earth and deep purple space backgrounds. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 63,
        "voiceover": "Some of the first Martians may never come home.",
        "scene": "First Martians gazing at a distant Earth — may never return — emotional",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Group of stick figures standing on rust-red Mars looking at a tiny blue-green Earth in the distant dark sky, the Earth tiny and far away, stick figures body language showing longing with arms at sides tilted heads and some with small tear marks on round faces, handwritten text MAY NEVER COME HOME in blue-electric letters at top, a red circle around the Earth, deep dark purple and blue starry sky. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 64,
        "voiceover": "Breakfast is grown on Mars.",
        "scene": "Stick figure eating breakfast with thought bubble showing food growing underground",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure sitting at a simple table eating breakfast, a thought bubble above showing the food growing underground on Mars, cross-section view below the table showing underground growing tunnels with vivid green plants under electric purple grow-lights, handwritten text GROWN ON MARS in electric yellow with red arrow, handwritten label BREAKFAST above the table, vivid greens underground contrasting with orange Mars surface above. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 65,
        "voiceover": "By 2055 the colony has enormous underground growing facilities.",
        "scene": "Vast underground growing cavern lit by electric grow-lights",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Wide cross-section view of a massive underground cavern carved into Martian rock, rows and rows of hand-drawn plants stretching into the distance under electric purple and blue artificial grow-lights, stick figures tending to the plants, the underground space glowing with vivid greens electric purples and warm yellows, handwritten text UNDERGROUND GROWING FACILITY with red arrow, the rust-red Mars surface visible above through the rocky ceiling. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 66,
        "voiceover": "Lit by artificial lights running on nuclear power.",
        "scene": "Nuclear power symbol connected to purple grow-lights powering the crops",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Hand-drawn nuclear power symbol in the centre connected by lines to rows of electric purple grow-lights above plants, power flowing through the connection shown as vivid electric yellow lightning bolt lines, handwritten text NUCLEAR POWER in bold electric yellow at top with red arrow, a stick figure engineer next to the power source with a clipboard and hard hat, deep dark Martian rock walls around, vivid yellows and purples. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 67,
        "voiceover": "Potatoes. Leafy greens. Certain grains.",
        "scene": "Three crops shown large — potato, leafy greens, wheat — the Martian menu",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Three large simple hand-drawn food items each in their own section of the frame, a big wobbly potato in warm brown on the left labelled POTATOES, vivid green leafy vegetables in the centre labelled LEAFY GREENS, golden wheat stalks on the right labelled CERTAIN GRAINS, all growing under electric purple underground grow-lights, handwritten labels with red arrows on each, deep dark underground rock background, vivid greens golds and purples. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 68,
        "voiceover": "All grown in Martian soil that has been carefully treated to remove the toxic perchlorates.",
        "scene": "Soil treatment process — toxic Martian dirt cleaned to grow food in",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Hand-drawn process diagram, left shows bucket of rust-red Martian soil with a skull-and-crossbones symbol and handwritten TOXIC PERCHLORATES in red, middle shows processing tank with chemical symbols and bubbling, right shows treated clean dark soil in a pot with a happy green plant growing, red arrows flowing left to right, handwritten labels at each stage, stick figure scientist in white coat overseeing the process with clipboard. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 69,
        "voiceover": "The food keeps you alive.",
        "scene": "Stick figure eating with zero joy — functional eating — food labelled keeps you alive",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure sitting at a plain table eating from a bowl with a completely flat expression, neutral dot eyes and straight line mouth, food labelled KEEPS YOU ALIVE in electric yellow with a red arrow, the food looking plain and colourless in contrast to the vivid colourful background, thought bubble above showing the stick figure imagining a delicious colourful Earth meal that then has a red X through it, warm orange habitat walls. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 70,
        "voiceover": "But it is not what you dreamed of.",
        "scene": "Stick figure deeply disappointed — dream vs reality split",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure with a deeply disappointed downturned mouth and sad drooping dot eyes looking at its tray of plain food, a thought bubble showing what it had dreamed of with a vivid colourful feast of steaks coffee and fruit in a fantasy bubble that is bright and colourful, the reality tray below grey and sparse, handwritten NOT WHAT YOU DREAMED OF in red at the top, contrasting colour palettes in dream vs reality emphasised. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 71,
        "voiceover": "There is no fresh fruit. No coffee. No steak.",
        "scene": "Fruit coffee and steak all crossed out with red X — nothing good on Mars",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Three panels in a row, left shows vivid colourful fresh fruit crossed out with a massive red X labelled NO FRESH FRUIT, centre shows a steaming coffee cup crossed out labelled NO COFFEE with stick figure weeping dramatically, right shows a juicy steak crossed out labelled NO STEAK with stick figure on knees in despair, all three against vivid warm colourful backgrounds to make the absence feel more painful, bold electric reds and warm colours. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 72,
        "voiceover": "Those things either don't exist on Mars or are so rare they are saved for special occasions.",
        "scene": "Rare food items locked in a glass museum case — special occasions only",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. A glass display case like a museum exhibit containing a tiny coffee cup a tiny piece of steak and a single orange all labelled with enormous price tags, handwritten text SPECIAL OCCASIONS ONLY with a red arrow, stick figures pressing their round-head faces against the glass with wide hungry dot eyes and drool drops, the display case glowing with warm yellow light, deep dark habitat background, vivid yellows and reds. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 73,
        "voiceover": "Water comes from ice extracted from below the Martian surface.",
        "scene": "Cross-section showing ice layer below Mars surface being drilled and melted",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Cross-section view, rust red Mars surface at top, below it a layer of blue-white ice, a drilling machine boring down to the ice with orange drill bit, water droplets flowing up through tubes into a collection tank above, handwritten label ICE BELOW SURFACE with red arrow pointing at the ice layer, WATER with blue arrow pointing at the collected water, stick figure operating the machine, vivid electric blues for the ice and water against the orange-red Martian ground. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 74,
        "voiceover": "Melted, filtered, recycled. Every drop used multiple times. Nothing is wasted.",
        "scene": "Water recycling loop — every drop used again and again — nothing wasted",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Three simple drawn panels connected by red arrows, panel 1: ice block melting labelled MELTED in blue, panel 2: water passing through a filter labelled FILTERED in green, panel 3: recycling loop symbol with water completing a circle labelled RECYCLED in yellow, a single vivid electric blue water droplet in the centre of the loop with the text NOTHING IS WASTED in bold electric green at top, deep dark purple and blue background. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 75,
        "voiceover": "You can call home.",
        "scene": "Stick figure reaching for a screen to call family — hopeful expression",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure in a small room reaching toward a glowing communication screen on the wall, an image of a stick figure family smiling and waving visible on the screen in warm yellow light, the caller's face showing a hopeful dot-eye expression with a small smile, handwritten text CALL HOME in electric yellow above the screen, warm orange habitat walls, small round porthole showing black starry Mars space outside. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 76,
        "voiceover": "But the call takes between 3 and 22 minutes to arrive depending on where Earth and Mars are in their orbits.",
        "scene": "Signal delay diagram showing 3 to 22 minute travel time across space",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Split frame, stick figure on Mars on the left side speaking into a microphone, a signal beam travelling slowly across deep dark purple space toward Earth on the right, a large hand-drawn clock face between them showing the travel time, bold handwritten text 3-22 MINUTE DELAY in electric yellow with red arrow, the orbits of Earth and Mars shown as curved dotted lines illustrating the varying distance. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 77,
        "voiceover": "A conversation takes 40 minutes for a single exchange.",
        "scene": "Timeline showing one exchange taking 40 full minutes — absurdly long",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Timeline diagram spanning the full width, Mars stick figure on the left says something at time zero, a signal arrow travels across to Earth on the right arriving 20 minutes later, Earth stick figure replies and the arrow travels back arriving at 40 minutes, bold handwritten 40 MINUTES at the top in red, two clocks drawn at each end showing start and end times, the long empty travel time in between shown as empty space. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 78,
        "voiceover": "You don't have conversations. You send messages. And wait. And wait.",
        "scene": "Stick figure sending message into void — slumped waiting — clock barely moving",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Two panels, left panel shows stick figure typing at a desk sending a message envelope flying into deep dark starry space, handwritten YOU SEND MESSAGES in yellow, right panel shows the same stick figure slumped completely flat on the desk with the screen still showing just ... and a blinking cursor, a clock on the wall with the hands barely moved, handwritten AND WAIT... AND WAIT... in large electric yellow above both panels. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 79,
        "voiceover": "Your family is aging without you.",
        "scene": "Family on Earth growing older while colonist stays away — time passing",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Side-by-side, right side shows a stick figure family on Earth growing progressively older across three time stamps, children getting taller adults getting wrinkle lines, left side shows the Mars stick figure frozen in a tiny habitat room not changing, deep dark space between them, handwritten text YOUR FAMILY — AGING WITHOUT YOU in electric yellow at top, a dotted line of separation between Mars and Earth sides, emotional quiet mood. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 80,
        "voiceover": "Birthdays pass. Funerals happen. Grandchildren are born.",
        "scene": "Three small scenes — birthday missed, funeral missed, grandchild born — all on a screen",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Three notification-style panels on a communication screen, top shows birthday cake and party stick figures with confetti labelled BIRTHDAY — MISSED in warm yellows and pinks, middle shows a dark muted funeral scene with stick figures gathered labelled FUNERAL — MISSED in cold blues, bottom shows a stick figure holding a tiny newborn baby in warm glowing yellow labelled NEW GRANDCHILD in green, Mars stick figure watching the screen with a complex emotional expression. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 81,
        "voiceover": "And you watch it all on a 22-minute delay from 225 million kilometres away.",
        "scene": "Everything on a 22-minute delay — 225 million km — time and distance felt",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Wide dramatic space scene, tiny Mars on the left with a stick figure watching a screen, enormous deep dark purple star-packed space between them, tiny blue-green Earth on the far right, a signal beam travelling slowly across with a clock drawn along the beam showing 22 MIN DELAY in red, bold handwritten 225 MILLION KM in electric yellow across the space between them, the stick figure looking tiny against the vast universe. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 82,
        "voiceover": "There is something else living on Mars does to you.",
        "scene": "Ominous shadow looming behind stick figure — something unknown",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure standing in habitat with a large ominous dark shadow looming behind it on the wall shaped like a question mark, red arrows pointing at the shadow, handwritten text SOMETHING ELSE... in red wobbly letters at the top, the figure turning its head slightly to see the shadow with wide cautious dot eyes, deep dark purple and navy blue habitat walls, electric reds and mysterious deep blues creating unease. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 83,
        "voiceover": "Something nobody fully knows the long term effects of yet.",
        "scene": "Scientists shrugging at a blank board with question marks — effects unknown",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Group of stick figures in white coats with clipboards all looking at a large blank board with only a question mark drawn on it, shrugging poses with palms up, handwritten text LONG TERM EFFECTS — UNKNOWN in big electric yellow letters at the top with red question marks scattered throughout, deep dark purple and blue background, bright white stars, frantic question marks in red and yellow filling the negative space. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 84,
        "voiceover": "Radiation.",
        "scene": "The word RADIATION filling the entire frame — nuclear symbol blazing",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. The word RADIATION in enormous bold hand-drawn letters filling the entire frame in vivid electric yellow with thick black outlines, the three-triangle radiation hazard symbol drawn large in orange-yellow next to the letters, the background a dramatic deep dark red and purple, jagged energy lines and zigzag patterns radiating outward from the letters, the word feeling dangerous and heavy, no stick figures just the word and symbol dominating. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 85,
        "voiceover": "Earth has a magnetic field that deflects the most dangerous cosmic rays.",
        "scene": "Earth's magnetic field as a blue shield deflecting cosmic rays",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Blue-green Earth in centre frame surrounded by a hand-drawn blue magnetic field bubble shield, jagged yellow cosmic rays flying in from the sides and bouncing off the blue shield, handwritten label MAGNETIC FIELD with red arrow pointing at the blue bubble, COSMIC RAYS label with arrow on the incoming bolts, stick figure on Earth surface visible inside the blue shield looking safe and protected, vivid electric blues and yellows, deep dark purple and navy space background. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 86,
        "voiceover": "Mars has almost no magnetic field.",
        "scene": "Mars with no shield — cosmic rays smashing directly through to the surface",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Orange-red Mars in centre frame with only a tiny faint broken dotted blue shield line barely visible around it, jagged electric yellow cosmic rays flying directly through and hitting the Mars surface unchallenged, handwritten label NO MAGNETIC FIELD in red with a red X over where the shield should be, stick figure on Mars surface getting hit by the rays with zigzag impact lines, deep dark purple and blue space background packed with stars. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 87,
        "voiceover": "Radiation on the Martian surface is 700 times higher than on Earth.",
        "scene": "700x bar chart — Mars radiation bar shoots impossibly off the top of the frame",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Bold massive handwritten 700x in enormous electric red letters filling the centre of the frame with a thick black outline, below it a split bar chart, Earth bar very short and green on the left, Mars bar impossibly tall in red shooting off the top of the frame with an arrow continuing upward, handwritten labels, stick figure looking at the Mars bar in shock with wide eyes and jaw dropped, deep dark purple starry background. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 88,
        "voiceover": "Every year you spend on Mars is equivalent to receiving hundreds of medical X-rays.",
        "scene": "Wall covered in hundreds of X-ray images — one year on Mars equals all of them",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Dozens and dozens of hand-drawn X-ray image rectangles covering the entire background like a wall each one showing a simple stick figure skeleton outline in electric blue-white, handwritten text ONE YEAR ON MARS equals HUNDREDS OF X-RAYS in bold electric yellow at the top with a red arrow, a stack of X-rays getting impossibly tall, stick figure with worried eyes standing next to the growing pile. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 89,
        "voiceover": "The long term effects — cancer risk, neurological damage, genetic changes — are still being studied.",
        "scene": "Clipboard list of long-term risks — cancer, neurological damage, genetic changes",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. A hand-drawn clipboard filling much of the frame with three items written in wobbly red handwriting: CANCER RISK with warning symbol, NEUROLOGICAL DAMAGE with warning symbol, GENETIC CHANGES with warning symbol, each with a red warning triangle drawn beside it, the words STILL BEING STUDIED handwritten at the bottom with a question mark, a stick figure scientist holding the clipboard with a deeply concerned expression, deep dark blue and purple starry background. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 90,
        "voiceover": "You signed the waiver before you left.",
        "scene": "Stick figure signing a legal waiver document before departing Earth",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure standing at a desk signing an enormous document labelled WAIVER in bold letters at the top, the document covered in tiny wobbly handwritten text and bullet points, the figure signing with a serious solemn expression, handwritten BEFORE YOU LEFT in electric yellow above the scene with a red arrow, blue-green Earth visible through a window behind it about to disappear from view, warm yellow interior light. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 91,
        "voiceover": "You knew the risks. But knowing a risk and living with it every day are very different things.",
        "scene": "Reading about risk vs living with it daily on Mars — completely different",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Left side stick figure reading a risk brochure calmly labelled KNOWING A RISK in yellow, right side same stick figure on Mars surrounded by invisible radiation zigzag lines filling the air looking anxious with a calendar of ticked-off days behind it labelled LIVING WITH IT in red, a large not-equal symbol between the two scenes in bold electric yellow, handwritten VERY DIFFERENT THINGS at the top. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 92,
        "voiceover": "The hardest part is not the radiation. It is not the food. It is not even the danger.",
        "scene": "Radiation food and danger symbols all crossed out — what is it then",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Multiple symbols all crossed out with red lines filling the frame, a radiation hazard symbol crossed out, a bowl of food crossed out, a danger warning triangle crossed out, a crashed rocket crossed out, each with NOT THIS written beside it in red, handwritten THE HARDEST PART IS NOT... in electric yellow at the top, stick figure pointing at all the crossed-out things shaking its round head, question mark energy building toward the right side. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 93,
        "voiceover": "It is the sky.",
        "scene": "The alien Mars sky filling the entire frame — IT IS THE SKY — devastating",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. The Mars sky taking up the entire frame, pale butterscotch pink and muted orange utterly alien with no blue no clouds no birds nothing familiar, just the strange pale dome above, at the very bottom a tiny stick figure looking up at it from rust-red ground looking very small against the vast alien sky, bold handwritten text IT IS THE SKY in massive electric yellow at the top with a strong wobbly underline, the emotional weight of missing home entirely in the composition. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 94,
        "voiceover": "Every morning you wake up and look out at that rust red landscape.",
        "scene": "Stick figure waking and looking out at the same rust red landscape again",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure waking up in a tiny bunk looking toward a small porthole window, outside the window is the same rust-red Martian landscape as always, the stick figure's expression is flat and tired with half-open dot eyes, a thought bubble above showing the same red landscape it has seen every single morning, handwritten text EVERY MORNING... in muted yellow at the top, warm orange habitat interior contrasting with the cold red world outside. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 95,
        "voiceover": "And there is no green.",
        "scene": "A green colour swatch with a red X — no green anywhere on Mars",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. A large vivid green colour swatch taking up most of the frame with a massive red X slashed through it, behind it the completely orange and rust-red Mars landscape with zero green visible anywhere, handwritten NO GREEN in huge bold red letters, stick figure looking at the crossed-out green with sad drooping dot eyes and a downturned mouth, the total absence of green emphasised by how vivid the swatch is before the X kills it. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 96,
        "voiceover": "No blue sky. No rain. No wind you can feel through your hair.",
        "scene": "Blue sky, rain and wind all crossed out — every comfort of Earth gone",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Three panels each with a vivid crossed-out image, left shows a blue sky with fluffy clouds crossed out labelled NO BLUE SKY, centre shows rain drops falling crossed out labelled NO RAIN, right shows a stick figure with hair blowing in wind crossed out labelled NO WIND, all three set against the barren rust-red Mars landscape below, the vivid colours of each thing making their absence hurt more, bold red X marks and labels. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 97,
        "voiceover": "No smell of grass. No ocean.",
        "scene": "Grass smell and ocean both crossed out — the senses Mars cannot give you",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Two large panels, left shows vivid green grass with wavy smell lines rising up in electric green crossed out with a massive red X labelled NO SMELL OF GRASS, right shows a vivid deep blue rolling ocean with waves and a seagull crossed out with a massive red X labelled NO OCEAN, stick figure in the middle looking at both crossed-out things with tear drops forming, the vivid colours of grass and ocean contrasting hard with the barren orange Mars background beneath the panels. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 98,
        "voiceover": "Studies on long duration spaceflight show that the absence of nature causes a specific kind of psychological deterioration.",
        "scene": "Scientist diagram showing nature deficit and psychological deterioration",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure scientist in white coat pointing at a chart on a wall, the chart shows a brain gradually losing colour from left to right as time without nature increases, a tree on the left side of the chart in vivid green slowly fading to grey and then nothing on the right, handwritten label NATURE DEFICIT in red at the top, bold text PSYCHOLOGICAL DETERIORATION below it with red arrow, deep dark purple background with white stars. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 99,
        "voiceover": "Scientists call it nature deficit.",
        "scene": "NATURE DEFICIT in bold text with a brain losing its colour like a battery draining",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Bold handwritten text NATURE DEFICIT in massive electric yellow letters at the top with wobbly underline, below it a large hand-drawn brain shown like a battery indicator, the left side full of colour with green trees blue sky and water, the right side drained to grey and empty, a red arrow pointing at the draining section, stick figure scientist with a clipboard pointing at the brain with a grave expression, deep dark purple starry background. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 100,
        "voiceover": "It builds slowly. Like a colour draining from the world.",
        "scene": "Colour slowly draining from the world — vivid on the left fading to grey on the right",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. A wide panoramic landscape that starts vivid and colourful on the far left with electric greens blues and yellows, and very gradually drains to grey and monochrome toward the far right, the same stick figure appears twice, on the left smiling with colour around it labelled FIRST MONTHS, on the right grey and hunched labelled LATER with the colour all gone, handwritten IT BUILDS SLOWLY in fading yellow text across the top. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 101,
        "voiceover": "Many Martian colonists report dreaming about Earth constantly.",
        "scene": "Stick figure asleep on Mars dreaming vivid colourful dreams of Earth",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure asleep in a tiny Mars bunk with Z-Z-Z above its round head, a huge vivid dream bubble rising above it showing an incredibly colourful Earth scene, green grass rolling hills blue sky sunshine birds and flowers all packed with electric greens blues and yellows, the stark contrast between the dull grey habitat room and the explosively colourful dream, handwritten DREAMING ABOUT EARTH CONSTANTLY in yellow inside the dream bubble. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 102,
        "voiceover": "About rain. About forests. About the smell of the ocean.",
        "scene": "Three vivid dream images — rain falling, a forest, the ocean smell",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Three dreamlike panels inside a big thought bubble, left panel shows stick figure standing in vivid blue rain with hands outstretched and a huge joyful smile labelled RAIN, centre panel shows stick figure walking through a vivid green forest with tall trees labelled FORESTS, right panel shows stick figure at the ocean edge with blue waves and green smell lines rising labelled THE SMELL OF THE OCEAN, all panels bursting with vivid greens blues and yellows, thick uneven black outlines throughout. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 103,
        "voiceover": "About things so ordinary back home that they never thought to appreciate them.",
        "scene": "Ordinary Earth things shown as precious — cup of coffee, open window, green garden",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Several simple ordinary Earth items drawn as if they were precious museum objects on pedestals, a steaming coffee cup on a pedestal, an open window with a breeze on a pedestal, a single flower on a pedestal, a patch of grass on a pedestal, each one glowing with warm yellow light and a handwritten label below, stick figure on Mars looking at drawings of these things with awe and tears, handwritten THINGS WE NEVER THOUGHT TO APPRECIATE in electric yellow at top. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 104,
        "voiceover": "But here is what those same colonists also say.",
        "scene": "Colonists leaning in together — something unexpected they all agree on",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Group of stick figures in a circle inside a Mars habitat all leaning inward conspiratorially with wide excited dot eyes and open-mouth expressions, speech bubbles with ... above each one suggesting they are about to share something remarkable, handwritten text BUT HERE IS WHAT THEY ALSO SAY in electric yellow at the top with a red arrow, warm orange habitat interior, a sense of wonder and shared secret in their body language. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 105,
        "voiceover": "On clear evenings when the dust storms settle — you can go to the observation dome.",
        "scene": "Stick figures walking to the observation dome on a clear calm evening",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figures walking toward a large glass dome structure on the Martian surface at evening time, the sky above the dome beginning to darken to deep dark purple with early stars appearing, the Martian ground calm and settled with no dust storm, the dome glowing softly from inside with warm yellow light, handwritten label OBSERVATION DOME with red arrow, handwritten CLEAR EVENING in the darkening purple sky, a sense of peaceful anticipation in the figures' forward-leaning postures. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 106,
        "voiceover": "And you can look up.",
        "scene": "Looking straight up at the Mars night sky from inside the dome",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. View from inside looking straight up through a dome ceiling, the dome frame visible as curved lines at the edges, above it the Mars night sky beginning to fill with an explosion of vivid stars in deep dark purple and navy blue, stick figures below with their heads tilted all the way back looking upward, necks craned, wide dot eyes reflecting starlight, handwritten AND YOU LOOK UP in electric yellow at the bottom of the frame below the figures, the sky above pulling the eye upward. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 107,
        "voiceover": "And the sky on Mars at night is something no human being who stayed on Earth will ever see.",
        "scene": "The Mars night sky — raw and impossibly clear — unlike anything on Earth",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. The Mars night sky filling the entire upper three-quarters of the frame, absolutely packed with thousands of bright white stars in every size, nebula wisps in vivid electric blue and purple, the Milky Way as a vivid band of yellow-white dust across the frame, the stars closer and more vivid than anything possible on Earth, a stick figure below tiny against the vast sky looking up with the most amazed open-mouthed expression, handwritten NO HUMAN ON EARTH WILL EVER SEE THIS in electric yellow. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 108,
        "voiceover": "No light pollution.",
        "scene": "NO LIGHT POLLUTION — perfect darkness making every star blaze",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Split comparison frame, left side shows a murky yellow-orange hazy Earth night sky with only a few dim stars visible labelled EARTH — LIGHT POLLUTION in orange with a sad face, right side shows the Mars night sky completely black and exploding with vivid bright stars in electric whites blues and purples labelled MARS — NO LIGHT POLLUTION in electric yellow with stars bursting outward, handwritten NO LIGHT POLLUTION in massive text across the top in electric yellow. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 109,
        "voiceover": "No atmosphere thick enough to blur the stars.",
        "scene": "Stars on Mars perfectly sharp and clear — no blur from thin atmosphere",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Two telescope views side by side, left shows a blurry smeared star through Earth's thick atmosphere labelled EARTH — BLURRED in orange, right shows the same star perfectly sharp and vivid through Mars thin atmosphere labelled MARS — CRYSTAL CLEAR in electric yellow with vivid sharp star points, the Mars telescope view filled with dozens of crisp bright stars in vivid whites blues and purples, handwritten NO BLUR at the top with a red arrow. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 110,
        "voiceover": "Just the raw universe.",
        "scene": "The raw universe — stars galaxies nebulae filling the frame completely",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. The entire frame filled with deep dark space, thousands of bright white stars, vivid electric blue and purple nebula clouds, a distant glowing galaxy, cosmic dust in warm oranges, the universe raw and enormous and beautiful, handwritten JUST THE RAW UNIVERSE in electric yellow at the bottom of the frame in awe-filled large letters, no stick figures just the overwhelming vastness of the universe drawn in vivid charming colours. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 111,
        "voiceover": "Closer and clearer than any human eye has ever seen it.",
        "scene": "The cosmos closer than ever — stars huge and vivid — stick figure eye wide with awe",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. A giant detailed hand-drawn eye filling the left side of the frame with a huge bright star reflected in its round pupil, around the eye the Mars night sky blazes with stars and nebulae, handwritten text CLOSER AND CLEARER THAN ANY HUMAN HAS EVER SEEN in electric yellow curving around the top, the stars in the reflection impossibly bright and vivid, the eye showing genuine wonder and awe in its dilated pupil. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 112,
        "voiceover": "And somewhere up there in that impossible black ocean of light — is a small pale blue dot.",
        "scene": "A single tiny pale blue dot in a vast black starfield — Earth",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. The entire frame filled with deep dark space packed with stars in vivid whites and yellows, and in the upper right area one single very small pale blue dot, a hand-drawn red arrow pointing at it with a label A SMALL PALE BLUE DOT in electric yellow handwriting, the tiny dot dwarfed by the vast black ocean of space around it, a stick figure below with one arm extended thumb up as if trying to cover the dot, the composition emphasising scale and smallness. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 113,
        "voiceover": "So small you could cover it with your thumb.",
        "scene": "A hand with thumb extended covering the tiny Earth dot completely",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. A simple hand-drawn stick figure hand with thumb extended filling most of the foreground, the thumb covering a tiny pale blue Earth dot visible in the deep dark starry space behind it, handwritten text YOU COULD COVER IT WITH YOUR THUMB in electric yellow around the hand, deep dark purple and navy space packed with bright stars everywhere the thumb is not covering, vivid stars visible peeking around the edges of the thumb, the scale and the emotion of the gesture combined. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 114,
        "voiceover": "That is Earth. That is everyone you have ever known. Everything you have ever loved.",
        "scene": "The pale blue dot with labels — everyone you know — everything you love",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Centre of the frame shows the small pale blue-green Earth dot, surrounding it in a circle are tiny handwritten labels connected by red lines, EVERYONE YOU HAVE EVER KNOWN, EVERYTHING YOU HAVE EVER LOVED, YOUR FAMILY, YOUR HOME, YOUR LIFE, all pointing at the tiny dot with red arrows, deep dark purple and navy space packed with stars everywhere, the dot tiny but radiating emotional gravity, electric yellows and blues in the labels. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 115,
        "voiceover": "Compressed into a single pixel of light.",
        "scene": "The word PIXEL — Earth reduced to a single dot of light — profound and small",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. A single tiny glowing pale blue pixel dot at the exact centre of the frame, surrounded by total deep dark space with cold white stars, the dot radiating a faint gentle glow, bold handwritten text A SINGLE PIXEL OF LIGHT in electric yellow curving around the dot, COMPRESSED written above it in red, the composition is quiet and vast and the dot looks terrifyingly small, the deep dark purple space emphasising the isolation. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 116,
        "voiceover": "And the colonists say that in that moment — every single one of them — feels the same thing.",
        "scene": "All colonists in the dome sharing the same feeling — unified under the stars",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Wide shot inside the observation dome looking outward at the Mars night sky, multiple stick figures all standing together looking up at the same spot in the starry sky, all of them with the same expression of profound quiet awe, small glowing lines connecting their hearts in a chain, handwritten EVERY SINGLE ONE OF THEM in electric yellow at the top, the Mars night sky blazing with vivid stars and nebulae above them, warm orange glow from the habitat behind them. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 117,
        "voiceover": "Not homesickness. Not regret.",
        "scene": "Crossed-out homesickness and crossed-out regret — something different and new",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Two large handwritten words crossed out, HOMESICKNESS in blue with a red strikethrough, REGRET below it in grey with a red strikethrough, beside the crossed-out words a stick figure shaking its head slowly, its expression not sad but something harder to name, questioning and profound, the frame open and expectant on the right suggesting something new is coming, deep dark purple starry sky behind, electric yellows and blues in the crossed-out text. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 118,
        "voiceover": "Something they don't have words for yet.",
        "scene": "Stick figure with an overflowing feeling they cannot name — no words exist",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure centre frame with a complex expression that is not quite sad not quite happy, something new and unnameable, a speech bubble above it with a blank space where words would normally go, just ... and a question mark, vivid colours flowing out from the figure like emotion without a name in electric blues yellows and soft purples, handwritten SOMETHING THEY DON'T HAVE WORDS FOR YET in electric yellow curving above, deep dark starry space background. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 119,
        "voiceover": "Something that might be the beginning of what it means to be from somewhere else.",
        "scene": "The first feeling of belonging somewhere other than Earth — new identity forming",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Stick figure standing on Mars looking at both Earth and Mars simultaneously, one foot on rust-red Martian ground one arm reaching toward the distant pale blue Earth dot in the sky, a glowing orange Mars symbol forming around the figure like a new identity, handwritten text THE BEGINNING OF BELONGING SOMEWHERE ELSE in electric yellow curving above, vivid deep purple space packed with stars, warm orange Mars ground below, the figure balanced between two worlds. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
    {
        "line": 120,
        "voiceover": "The first humans who are not from Earth. But from Mars. Subscribe to Unknown Origins.",
        "scene": "First Martians standing proud on Mars — then subscribe button — emotional close",
        "prompt": "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Group of stick figures standing tall and proud on rust-red Mars, arms raised, the deep dark purple star-packed sky above them with a tiny Earth visible in the distance, handwritten text THE FIRST HUMANS FROM MARS in bold electric yellow above them, below the figures a large hand-drawn red SUBSCRIBE button with UNKNOWN ORIGINS written above it and a red arrow pointing at it, warm orange Martian glow on the ground, vivid purples blues and yellows, triumphant and emotional composition. No realistic shading. No 3D. No white or plain backgrounds. 16:9 aspect ratio."
    },
]

# Calculate timestamps evenly across 7m58s (478 seconds) for 120 scenes
TOTAL_SECONDS = 478  # 7m58s
NUM_SCENES = len(SCENES)

def seconds_to_timestamp(s):
    m = int(s) // 60
    sec = int(s) % 60
    return f"{m}m{sec:02d}s"

def build_batch():
    interval = TOTAL_SECONDS / NUM_SCENES  # ~3.98s per scene
    output = []
    for i, scene in enumerate(SCENES):
        start_s = i * interval
        end_s = (i + 1) * interval
        start_ts = seconds_to_timestamp(start_s)
        end_ts = seconds_to_timestamp(end_s)
        filename = f"astrova_{end_ts}.png"
        output.append({
            "line": scene["line"],
            "start": start_ts,
            "end": end_ts,
            "voiceover": scene["voiceover"],
            "scene": scene["scene"],
            "prompt": scene["prompt"],
            "filename": filename
        })
    return output

def print_formatted(batch):
    print("=" * 80)
    print("UNKNOWN ORIGINS — LIFE ON MARS 2055")
    print("120 SCENE PROMPTS — HIGGSFIELD AI NANO BANANA PRO")
    print(f"Total duration: 7m58s | Scenes: {NUM_SCENES} | Rate: ~3.98s per scene")
    print("=" * 80)
    print()
    for item in batch:
        print(f"[{item['line']}] {item['start']}")
        print(f"VOICEOVER: {item['voiceover']}")
        print(f"SCENE: {item['scene']}")
        print(f"PROMPT: {item['prompt']}")
        print(f"FILENAME: {item['filename']}")
        print()

def save_json(batch, path="higgsfield_prompts.json"):
    with open(path, "w") as f:
        json.dump(batch, f, indent=2)
    print(f"Saved {len(batch)} prompts to {path}")

def print_filenames(batch):
    print("\n--- BATCH FILENAME LIST ---")
    for item in batch:
        print(item["filename"])

def print_prompts_only(batch):
    """Print just the prompts one per line for easy paste into Higgsfield"""
    print("\n--- PROMPTS ONLY (paste one at a time into Higgsfield) ---\n")
    for item in batch:
        print(f"# [{item['line']}] {item['filename']}")
        print(item["prompt"])
        print()

if __name__ == "__main__":
    import sys
    batch = build_batch()

    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == "json":
            save_json(batch)
        elif mode == "filenames":
            print_filenames(batch)
        elif mode == "prompts":
            print_prompts_only(batch)
        elif mode == "full":
            print_formatted(batch)
    else:
        print_formatted(batch)
        print_filenames(batch)
