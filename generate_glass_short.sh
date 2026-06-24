#!/bin/bash

HF=/opt/homebrew/lib/node_modules/@higgsfield/cli/vendor/hf

mkdir -p output_glass_short

gen() {
  local num=$1
  local prompt=$2
  local filename=$3
  if grep -q "https://" "output_glass_short/image_${num}.txt" 2>/dev/null; then
    echo "Skipping scene $num (already done)"
    return
  fi
  echo "Generating scene $num..."
  local attempts=0
  local job_id=""
  until [[ -n "$job_id" ]]; do
    job_id=$($HF generate create nano_banana_2 --prompt "$prompt" --json 2>/dev/null | tr -d '[]" \n')
    if [[ -z "$job_id" ]]; then
      attempts=$((attempts + 1))
      if [ $attempts -ge 3 ]; then
        echo "FAILED scene $num after 3 attempts"
        return
      fi
      echo "Retrying scene $num (attempt $attempts)..."
      sleep 5
    fi
  done
  echo "Waiting for scene $num..."
  $HF generate wait "$job_id" > "output_glass_short/image_${num}.txt" 2>&1
  echo "Done $num - $filename"
}

gen 1 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue and purple space background packed with bright white stars. Giant bold wobbly handwritten text THERE IS A PLANET WHERE IT RAINS GLASS filling most of the frame in bright yellow with thick red outline. Small stick figure at bottom looking up at the words mouth wide open shocked. Red arrows pointing upward dramatically. Lots of colour electric blues vivid purples. No white backgrounds. 9:16 vertical aspect ratio." "short1_scene01.png"

gen 2 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark purple background. Hundreds of sharp glass shards flying horizontally across entire frame with massive bold red speed lines behind them. NOT DOWN label crossed out with red X. SIDEWAYS label in giant yellow letters with thick red outline. 8700 KM/H in massive bold red text with giant arrow. Stick figure at right side arms flying back being hit by force mouth screaming. Dramatic energy speed lines everywhere. No white backgrounds. 9:16 vertical aspect ratio." "short1_scene02.png"

gen 3 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple starry space background packed with bright white stars. Giant glowing deep blue planet centre frame looking peaceful and beautiful. Bold wobbly handwritten HD 189733b label with red arrow pointing at planet. LOOKS JUST LIKE EARTH label below in yellow letters thick red outline. Stick figure in tiny rocket nearby pointing at planet with curious expression. Lots of colour electric blues glowing purples. No white backgrounds. 9:16 vertical aspect ratio." "short1_scene03.png"

gen 4 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple space background packed with glowing stars and soft nebula clouds. Giant deep blue planet filling frame glowing with soft warm light looking calm and peaceful. DEEP BLUE label in gentle yellow wobbly text. ALMOST PEACEFUL label below with soft glow. Stick figure floating nearby eyes wide in wonder arms out. Dreamy calm energy completely different mood. Lots of colour soft blues glowing purples. No white backgrounds. 9:16 vertical aspect ratio." "short1_scene04.png"

gen 5 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark purple background. Stick figure exploding into pieces from glass shards hitting from all sides. Glass shards flying at extreme speed across entire frame. Dramatic speed lines radiating from impact point. SANDBLASTED OUT OF EXISTENCE label in giant red letters thick yellow outline. Before and after shown small intact stick figure becoming cloud of pieces. Red arrows everywhere. Extreme dramatic energy. No white backgrounds. 9:16 vertical aspect ratio." "short1_scene05.png"

gen 6 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple background. Two sections stacked. Top half NOT SLOWLY in giant text with massive red X through it stick figure slowly fading crossed out. Bottom half INSTANTLY in enormous bold yellow letters thick red outline with stick figure vanishing in single dramatic flash and explosion lines. Lightning bolt between sections. Speed lines everywhere. Dramatic contrast energy. Lots of colour electric blues vivid reds. No white backgrounds. 9:16 vertical aspect ratio." "short1_scene06.png"

gen 7 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark purple background. Massive swirling glass hurricane storm filling entire frame with sharp shards spiralling outward. IT HAS NEVER ONCE STOPPED label in giant red letters thick yellow outline at top. NOT FOR A SINGLE SECOND label in bold yellow below. Storm arrows showing circular never-ending motion. Infinity symbol on storm. Stick figure tiny at bottom looking up in terror. Dramatic energy. No white backgrounds. 9:16 vertical aspect ratio." "short1_scene07.png"

gen 8 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple background packed with stars. Giant horizontal timeline arrow stretching across entire frame. BILLIONS OF YEARS label in enormous bold yellow letters thick red outline. Storm symbol repeating along entire timeline showing it never stopped. Tiny Earth shown at end of timeline for scale comparison. Stick figure jaw dropped pointing at the timeline overwhelmed. Red arrows emphasising scale. Lots of colour. No white backgrounds. 9:16 vertical aspect ratio." "short1_scene08.png"

gen 9 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple starry space background packed with bright white stars glowing planets and colourful nebulas. Giant glowing subscribe button centre frame with bold wobbly FOLLOW UNKNOWN ORIGINS label in giant yellow letters thick red outline. NEW VIDEO EVERY WEEK label below in red. Stick figure pressing subscribe button with huge excited expression. Stars and planets surrounding. YOU ARE NOT READY label at top in bold red. Dramatic energy speed lines radiating outward. Lots of colour. No white backgrounds. 9:16 vertical aspect ratio." "short1_scene09.png"

gen 10 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple starry space background packed with bright white stars and glowing nebulas. Giant deep blue planet filling centre of frame with visible glass shards swirling around it at extreme speed red speed lines showing direction. HD 189733b label with red arrow. IT RAINS GLASS label in massive bold yellow letters thick red outline filling top of frame. UNKNOWN ORIGINS label at bottom bold. Stick figure tiny in corner staring in awe. Epic dramatic final energy. No white backgrounds. 9:16 vertical aspect ratio." "short1_scene10.png"

echo ""
echo "All 10 scenes generated! Check the output_glass_short/ folder."
