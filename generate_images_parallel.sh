#!/bin/bash

# Higgsfield image generation script - 173 images in parallel batches of 10
# Run this on your Mac: bash generate_images_parallel.sh

STYLE="Amateur hand-drawn stick figure style like MS Paint. White background. Thick uneven wobbly outlines. Simple stick figures with round heads and dot eyes. Basic facial expressions. No shading. No 3D. No realism. No anime. Intentionally bad drawing. Simple flat colours."

mkdir -p output

run() {
  local num=$1
  local prompt=$2
  echo "Generating image $num..."
  higgsfield generate create nano_banana_2 --prompt "$STYLE $prompt" --wait > output/image_${num}.txt 2>&1
  echo "Done $num"
}

export -f run
export STYLE

# All 173 prompts - run in parallel batches of 10
parallel -j10 run {1} {2} ::: \
  1 "A stick figure person lying in bed under a wobbly blanket, eyes closed with ZZZ floating above. A light switch on the wall with a red arrow. Simple moon and stars outside a lopsided window." \
  2 "A stick figure lying in bed. A thought bubble above their head that is completely empty. Wobbly lines." \
  3 "A wonky circle Earth at the bottom. A tiny boxy space station above it. Dotted line showing distance labelled 408KM in handwriting. Six tiny stick figures visible inside the station." \
  4 "A stick figure astronaut floating inside a box with question marks all around their head. Small porthole window with scribbled stars outside. Confused expression." \
  5 "Split drawing. Left side: moon and dark sky labelled NIGHT. Right side: big yellow blazing sun labelled ALSO NOW with a red arrow. Stick figure astronaut looking baffled in the middle." \
  6 "A wonky circle representing Earth. A tiny boxy ISS with rectangle solar panels orbiting it. Dotted curved arrow showing orbit path. 90 MINS written in wobbly handwriting." \
  7 "A stick figure astronaut with a shocked open mouth. Around them 16 tiny badly drawn suns rising and setting. x16 written in wobbly red handwriting." \
  8 "The number 16 written huge and wobbly in the centre. A stick figure below looking up with shocked expression and arms raised. Red underline." \
  9 "A boxy space station with a big red question mark floating next to it. Label MOST EXPENSIVE THING EVER in wobbly handwriting. Stick figure shrugging inside." \
  10 "A stick figure head in the centre. Inside the head: a tiny bed drawing, a brain scribble, and a clock. All crammed in and wobbly. Red arrows pointing outward labelled SLEEP? TIME? MIND?" \
  11 "A red arrow pointing to a tiny boxy room inside a space station drawing. Label WHERE THEY SLEEP in wobbly handwriting." \
  12 "A very tall thin box the size of a phone booth with a stick figure squished inside. Label PHONE BOOTH SIZE with a red arrow." \
  13 "Inside a small boxy room: a sleeping bag strapped to the wall, a tiny laptop, a small porthole window. Simple labels drawn in handwriting." \
  14 "A mattress with a big red X through it. Label NO MATTRESS in wobbly handwriting." \
  15 "A bed frame with a big red X through it. Label NO BED FRAME in wobbly handwriting." \
  16 "A stick figure floating horizontally in mid air inside a box. Wavy lines around them showing floating. Label YOUR BODY FLOATS." \
  17 "A stick figure zipped up inside a sleeping bag floating in mid air. Arms at sides. ZZZ above. Label JUST HANG THERE." \
  18 "A very narrow rectangular box shaped like a coffin. A stick figure inside with eyes open. Label LIKE A COFFIN in wobbly handwriting." \
  19 "A tiny box with a stick figure squished and cramped inside. Label THAT SMALL with a red arrow showing how tiny it is." \
  20 "A stick figure floating with arrows pointing in all directions labelled UP? DOWN? LEFT? RIGHT? Big question mark above head." \
  21 "A stick figure lying on a mattress on Earth. A brain above them with a speech bubble saying REST COMING. Gravity arrow pointing down." \
  22 "A floating stick figure in space with a big red X next to a mattress and gravity arrow. Label NONE OF THAT EXISTS." \
  23 "A large ear with confused zigzag lines and question marks coming out of it. Label VESTIBULAR SYSTEM CONFUSED." \
  24 "A stick figure floating with a confused wavy expression. Label SCOTT KELLY and speech bubble saying JUST WRONG." \
  25 "A stick figure with a neutral confused expression. Two labels with arrows: NOT SCARY pointing one way and JUST WRONG pointing another." \
  26 "A stick figure floating and slowly spinning. Spiral arrow around them. Label SOMEONE KEEPS SPINNING YOU." \
  27 "A stick figure in a sleeping bag with both arms floating straight up above them. Straps around the arms. Label STRAP THEM DOWN." \
  28 "A stick figure waking up in a sleeping bag. Two hands floating right in front of their face. Big shocked wide eyes. 3AM written nearby. Stars outside porthole." \
  29 "A stick figure staring at their own hands floating in front of their face. STARTLING written in wobbly letters with a red exclamation mark." \
  30 "Close up of a stick figure face with a very puzzled expression. Label THE STRANGEST PART with a red arrow pointing at the face." \
  31 "A simple stick figure body outline. Big arrows pointing upward from legs and torso toward the head. Label 2 LITRES OF FLUID with a red arrow." \
  32 "A stick figure with very thin stick legs compared to a normal body. The legs labelled BIRD LEGS with arrows pointing to them." \
  33 "A stick figure with a big puffy round face much larger than normal. Label FACE SWELLS with a red arrow." \
  34 "A stick figure with a red stuffed up nose. Wavy stink lines coming from the nose. Label PERMANENT HEAD COLD." \
  35 "A sick stick figure with watery eyes and red nose. Label WORST SINUS INFECTION OF THEIR LIFE. Miserable face." \
  36 "A plate of food with a nose that has an X through it. Label CANT SMELL with a red arrow." \
  37 "A plate of food with a tongue that has an X through it. Label CANT TASTE with a red arrow." \
  38 "A stick figure head with pressure arrows pressing in from all sides. Label RELENTLESS HEADACHE in red wobbly writing." \
  39 "A stick figure with huge wide eyes and raised eyebrows. Label BUT HERE IS WHERE IT GETS STRANGE with a red arrow." \
  40 "A brain with a tiny cleaning crew inside it. Arrows showing waste being flushed out. Label GLYMPHATIC SYSTEM and UNIVERSITY OF ROCHESTER 2013." \
  41 "A brain with cells shrinking slightly shown by arrows. Fluid rushing through gaps. Label TOXIC WASTE FLUSHED OUT. Small protein shapes labelled ALZHEIMERS." \
  42 "A stick figure lying flat. A gravity arrow pointing down. Fluid flowing smoothly through a simple brain diagram. Label THIS WORKS ON EARTH." \
  43 "A stick figure floating horizontally in space. Fluid shown going the wrong direction in brain with confused arrows. Label DOESNT FLOW THE SAME." \
  44 "A simple skull outline with a brain drawn inside shifted upward. Red arrow showing it moved up. Label BRAIN SHIFTS UPWARD." \
  45 "A big 63% written in wobbly numbers. A simple brain diagram next to it showing changes. Label MEASURABLE CHANGES after 6 months." \
  46 "A stick figure astronaut with droopy tired eyes. Label SLEEP IS HARD IN SPACE with a sad face." \
  47 "A stick figure with a surprised expression. Label SLEEP IS DOING SOMETHING DIFFERENT with a red arrow." \
  48 "A space station with a big blazing sun suddenly appearing outside the window. Red lines showing radiation. Label EVERY 90 MINUTES." \
  49 "A huge yellow sun with intense rays. Label FULL UNFILTERED DIRECT SUNLIGHT in wobbly handwriting." \
  50 "A simple atmosphere layer diagram with Earth. A red X through the atmosphere layer. Label NO ATMOSPHERE." \
  51 "A sky with a red X through the clouds. Label NO CLOUDS." \
  52 "Solar radiation lines hitting a space station window. Label PURE SOLAR RADIATION with a red arrow." \
  53 "A stick figure body with a clock drawn inside the chest area. Label YOUR BODY HAS A CLOCK." \
  54 "A circle divided into 24 hours. Half labelled AWAKE with a sun. Half labelled ASLEEP with a moon. Label CIRCADIAN RHYTHM." \
  55 "A single arrow pointing at a light bulb. Label SET BY ONE SIGNAL." \
  56 "A big simple drawn sun. Label LIGHT written in large wobbly letters below it." \
  57 "A simple brain diagram with a tiny cluster of dots highlighted. Label SUPRACHIASMATIC NUCLEUS with a wobbly red arrow." \
  58 "A simple eye with a light beam hitting it. An arrow going from the eye to a brain. Label IT IS DAY." \
  59 "An upward arrow labelled CORTISOL UP. A stick figure standing alert with straight posture." \
  60 "A downward arrow labelled MELATONIN DOWN. Simple drawing." \
  61 "A stick figure standing very upright with alert wide eyes. Label BE ALERT." \
  62 "A moon and dark sky. An upward arrow labelled MELATONIN RISES." \
  63 "A thermometer with the level going down. Label CORE TEMP DROPS." \
  64 "A stick figure with heavy droopy eyes. Label YOU GET SLEEPY. Zs floating nearby." \
  65 "The ISS surrounded by 16 tiny alternating sun and moon symbols. Label 16 TIMES A DAY with a red arrow." \
  66 "A simple timeline showing SUN DARK SUN DARK SUN DARK rapidly alternating. Label NOTHING TO DO WITH 24 HOURS." \
  67 "A brain with question marks all around it. Confused expression on a stick figure below. Label BRAIN DOESNT KNOW WHAT TO DO." \
  68 "A simple bar chart. One bar labelled 6 HOURS short. One bar labelled 8 HOURS taller. NASA SCHEDULE label on the taller one." \
  69 "A wavy broken sleep line graph. Gaps and interruptions shown clearly. Label FRAGMENTED with arrows." \
  70 "A stick figure lying in a sleeping bag staring at the ceiling with wide open eyes. Label DIFFICULT TO START." \
  71 "A stick figure waking up multiple times shown as three frames. Each time eyes pop open. Label FREQUENT WAKING." \
  72 "A pill bottle with a label on it. A stick figure reaching for it. Label PRESCRIPTION SLEEP MEDICATION." \
  73 "A calendar. Some days highlighted. Label NOT OCCASIONALLY with a red X." \
  74 "The word REGULARLY written in big wobbly letters. Red underline." \
  75 "The ISS interior with new LED panels. Left side showing cool blue light. Right side showing warm amber light. Label NEW LEDS 2016." \
  76 "A small green checkmark. Label IT HELPED in small wobbly writing." \
  77 "A small green checkmark with a red X below it. Label BUT DIDNT SOLVE IT." \
  78 "Four simple icons in a row: a sun, a thermometer, a plate of food, a stick figure exercising. Label NOT JUST LIGHT with a red arrow." \
  79 "On Earth: sun, meal, exercise, temperature all lined up with arrows showing they align. Label ALL ALIGN ON EARTH." \
  80 "The same four icons but all jumbled and scrambled. Red arrows pointing in wrong directions. Label SCRAMBLED IN SPACE." \
  81 "A thermometer stuck showing 22 degrees. A clock next to it. Label CONSTANT 22 DEGREES AROUND THE CLOCK." \
  82 "A moon with a thermometer next to it showing warm temperature. Red X through the cold symbol. Label NO GETTING COLD AT NIGHT." \
  83 "Label CIRCADIAN MISALIGNMENT written in large wobbly letters with a red arrow pointing to a confused stick figure." \
  84 "A numbered list with 3 items: 1 RADIATION 2 MUSCLE LOSS 3 SLEEP with a red circle around number 3." \
  85 "A stick figure waving their hand dismissively. Label NOT A MINOR INCONVENIENCE with emphasis lines." \
  86 "TOP 3 HEALTH RISK written in huge wobbly letters. Red underline. Exclamation mark." \
  87 "A stick figure with a mischievous expression and a pointed finger raised. Label BUT HERES WHAT I HAVENT TOLD YOU." \
  88 "A list of problems: MISALIGNED CLOCKS, SWOLLEN FACES, MEDICATION. Then a big question mark at the bottom." \
  89 "The word MAGIC written in big wobbly glowing letters. Stars and sparkles around it. Simple style." \
  90 "A clock showing 7:30. A stick figure astronaut stretching and finishing work. Label PERSONAL TIME with an arrow." \
  91 "Multiple stick figure astronauts all floating in the same direction toward a window. Arrows showing movement." \
  92 "A large window with Earth glowing outside it. A stick figure silhouette looking through. Label AT THE WINDOW." \
  93 "A dome shape with 7 circles representing windows. Earth visible through them. Label CUPOLA with a red arrow." \
  94 "A simple station drawing with a star next to the Cupola dome. Label MOST IMPORTANT PIECE OF EQUIPMENT." \
  95 "A science beaker with a red X. Label NOT FOR SCIENCE." \
  96 "A simple brain/head outline with a glowing light inside it. Label WHAT IT DOES TO THE HUMAN MIND." \
  97 "A stick figure astronaut floating upward toward a circular window. Motion lines showing movement upward." \
  98 "A stick figure looking downward through a window. Earth below them. Simple curves showing the planet." \
  99 "A stick figure at a window with a completely blank empty expression. Just staring. Nothing in thought bubble." \
  100 "Looking down at Earth from above. City lights shown as tiny dots and lines glittering in darkness. Label LIKE SCATTERED STARS." \
  101 "A cloud system with jagged lightning bolts drawn inside it. Label LIGHTNING STORMS PULSE SILENTLY. No sound lines." \
  102 "A simple rectangle representing a continent. A line sweeping across it half dark half light. Label TERMINATOR LINE." \
  103 "A space station with speed lines behind it. Label 17500 MPH and CONTINENT IN MINUTES in wobbly handwriting." \
  104 "A stick figure astronaut with a speech bubble saying ORBITAL PERSPECTIVE. Label RON GARAN with an arrow." \
  105 "A globe with no country border lines drawn on it. Just the coastlines. Label NO BORDERS." \
  106 "The same globe with NO LINES BETWEEN COUNTRIES label. Simple drawing." \
  107 "A small planet Earth floating in a big black space background with just a few stars. Label ONE FRAGILE BEAUTIFUL PLANET." \
  108 "A stick figure with a changed expression before and after. Arrow between them showing something shifted." \
  109 "A stick figure with a thought bubble. Inside the contents have changed. Label IT CHANGED WHAT HE BELIEVED." \
  110 "The words OVERVIEW EFFECT written in large wobbly handwriting. A red arrow pointing to a stick figure astronaut." \
  111 "Multiple stick figure astronauts with identical speech bubbles all saying the same thing. Label EVERY ASTRONAUT SAME SHIFT." \
  112 "Before and after stick figures. Switch flipped between them. Label NOT GRADUAL - SUDDEN." \
  113 "A large light switch with a hand flipping it from OFF to ON. Bold lines. Label LIKE A SWITCH BEING FLIPPED." \
  114 "A stick figure on a simple drawn moon surface. A huge overwhelming glow radiating outward. Stars connected by lines. Label EDGAR MITCHELL." \
  115 "A stick figure at a desk surrounded by papers and books. Writing notes. Label SPENT REST OF HIS LIFE TRYING TO EXPLAIN IT." \
  116 "A stick figure shrugging with arms out. Speech bubble: YOU DONT HAVE TO AGREE. But pointing at a heavy weight symbol." \
  117 "Split drawing. Left side: stars and wonder. Right side: dark shadows. Label BUT NOT ONLY WONDER." \
  118 "A stick figure with arms crossed and closed off body language. Face looking away slightly. Label RELUCTANT TO TALK ABOUT." \
  119 "A stick figure astronaut with a calendar showing 215 DAYS marked. Label MIKE LOPEZ-ALEGRIA." \
  120 "A list with PHYSICAL crossed out and QUIET circled. Label THE HARDEST PART WASNT PHYSICAL." \
  121 "An empty room with one stick figure sitting alone. Very simple. Lots of empty space around them. Label THE QUIET." \
  122 "A stick figure with a heavy weight dropping down onto their shoulders. Label THE WEIGHT OF WHERE HE WAS." \
  123 "A stick figure inside a metal tube shape. Bolts on the walls. Label YOU ARE IN A METAL TUBE." \
  124 "Speed lines behind the metal tube. Label 5 MILES PER SECOND." \
  125 "Outside a window: a skull and crossbones symbol. Label VACUUM KILLS YOU IN UNDER 2 MINUTES. Red border." \
  126 "One stick figure floating alone in space. A big distance arrow. Label 250 MILES FROM EVERYONE." \
  127 "A calendar with 6 months marked. A tiny house crossed out far away. Label WILL NOT GO HOME FOR 6 MONTHS." \
  128 "A timeline with a label at 3/4 mark: THIRD QUARTER PHENOMENON. Wobbly handwriting." \
  129 "A simple graph line going down sharply at the 3/4 point. Labels: MOTIVATION DOWN, MOOD DOWN, CONFLICT UP." \
  130 "Three drawings in a row: Antarctic crew, submarine crew, astronaut crew. All with same sad expression. Label SAME PATTERN." \
  131 "A stick figure holding up a wall. Label CAN TOLERATE ALMOST ANYTHING FOR A WHILE. Strain lines." \
  132 "The same stick figure but something small slipping or sliding. Label SOMETHING SLIPS." \
  133 "A simple Mars circle in red. A timeline below it with marker at 18 MONTHS. Label MARS MISSION." \
  134 "A timeline with the 18 MONTH mark circled in red. Label IT HITS HERE." \
  135 "A door with a big X through it and a lock. Label NO EMERGENCY RETURN." \
  136 "A clock with 20 MIN label. A speech bubble going across a long distance with 40 MIN EXCHANGE label." \
  137 "A stick figure shrugging with hands up. Label SO WHAT DO THEY DO? Question marks around them." \
  138 "Two stick figures with matching notepads. One labelled ASTRONAUT one labelled PSYCHOLOGIST. Their notes are identical." \
  139 "A stick figure drawing a circle or routine symbol. Label THEY CREATE RITUALS." \
  140 "Stick figures floating around a table with food pouches. Label CREW DINNERS with a simple table drawing." \
  141 "Multiple stick figures seated together at meal time. Label SITTING TOGETHER with an arrow." \
  142 "A body clock diagram with an arrow pointing to it saying DAY ENDING. Label THE RITUAL TELLS YOUR BODY." \
  143 "A moon symbol with ZZZ. Label REST IS COMING in speech bubble." \
  144 "Small items floating: a photograph, a book, a small object. Label PERSONAL ITEMS FROM HOME." \
  145 "A stick figure writing in a journal book. Pen in hand. Words floating out of the journal." \
  146 "A calendar with every day marked. Label SCOTT KELLY EVERY SINGLE DAY." \
  147 "Words flowing from a stick figure head into a book page. Label PROCESSING INTO WORDS." \
  148 "A book with a red X. Label NOT FOR THE RECORD." \
  149 "A brain with a clear bright light inside. Clarity lines radiating. Label MENTAL CLARITY." \
  150 "A stick figure astronaut with a very long timeline underneath them. Label SERGEI KRIKALEV. MORE TIME IN SPACE THAN ALMOST ANYONE." \
  151 "One stick figure alone in a large empty dark space. Just floating. Label THE ISOLATION." \
  152 "Wavy silence lines radiating outward. No sound symbols. Label THE SILENCE." \
  153 "A tiny Earth sphere far away in the distance. Label THE ABSENCE OF EARTH." \
  154 "A stick figure at a window. Through the window a city is visible below with simple dot lights. Label WATCH A CITY PASS BELOW." \
  155 "A city drawn simply from above as a grid of streets and dots of light. Label ANY CITY." \
  156 "Stick figures inside buildings turning off lights. Simple house shapes. Label ALL THE PEOPLE INSIDE IT." \
  157 "Stick figures in beds with blankets. ZZZ above each one. Label GOING TO SLEEP." \
  158 "Simple house shapes with lights going off one by one shown by X symbols. Label TURNING OFF THEIR LIGHTS." \
  159 "A stick figure astronaut with a small warm smile. Label MADE HIM FEEL LESS ALONE." \
  160 "View from above: a city glowing with lights. A tiny space station visible above it. Label SOMEONE IS WATCHING YOUR CITY GLOW." \
  161 "A stick figure astronaut face with 16 tiny suns around it. Label 16 SUNRISES ALREADY TODAY. Tired eyes." \
  162 "A stick figure with an exaggerated puffy swollen face. Label FACE IS SWOLLEN. Red arrows." \
  163 "A brain with question marks and unsolved problem symbols floating around it. Label PROBLEMS NO ONE HAS SOLVED." \
  164 "A stick figure with arrows pointing everywhere labelled WHAT TIME IS IT? and WHICH WAY IS UP? Confused face." \
  165 "A stick figure floating in front of a large window looking down at city lights far below. Stars above." \
  166 "Stars in space with a label THE FRONTIER in big wobbly letters. Stick figure pointing outward toward space." \
  167 "A book with THE NEXT CHAPTER written on the cover in wobbly handwriting." \
  168 "A stick figure arm reaching upward toward stars. Simple reaching gesture." \
  169 "Multiple stick figures who have been to space. All pointing backward with thumbs behind them. Label THEY KEEP SAYING." \
  170 "Multiple stick figure astronauts all turning to look backward at a glowing Earth sphere. Label EVERY ONE OF THEM LOOKED BACK." \
  171 "Multiple stick figures with identical speech bubbles all containing the same symbol. Label EVERY ONE SAID THE SAME THING." \
  172 "A small simple Earth sphere in the centre of lots of empty space. Very small. Label SMALLER THAN THEY EXPECTED." \
  173 "A glowing Earth sphere drawn simply but warmly. Glow lines around it. Label MORE BEAUTIFUL THAN THEY HAD WORDS FOR."

echo ""
echo "All 173 images generated! Check the output/ folder."
