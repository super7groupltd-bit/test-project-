#!/bin/bash

HF=/opt/homebrew/lib/node_modules/@higgsfield/cli/vendor/hf

mkdir -p output_glass_short2

gen() {
  local num=$1
  local prompt=$2
  if grep -q "https://" "output_glass_short2/image_${num}.txt" 2>/dev/null; then
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
  $HF generate wait "$job_id" > "output_glass_short2/image_${num}.txt" 2>&1
  echo "Done $num"
}

gen 1 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple starry space background packed with bright white stars. Giant glowing deep blue planet filling centre of frame looking calm and beautiful almost identical to Earth. LOOKS HARMLESS label in giant yellow letters thick red outline at top. Stick figure in tiny rocket nearby smiling pointing at planet relaxed expression. Soft dreamy peaceful energy. Lots of colour electric blues glowing purples. No white backgrounds. 9:16 vertical aspect ratio."

gen 2 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark purple background with ominous red glow creeping in from edges. Stick figure centre frame face changing from smile to absolute terror eyes enormous mouth wide open. SOMETHING IS VERY WRONG label in giant red letters thick yellow outline filling top of frame. Warning symbols and red arrows radiating outward. Speed lines showing sudden dread. Dramatic shift in energy. Lots of colour vivid reds electric purples. No white backgrounds. 9:16 vertical aspect ratio."

gen 3 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark purple background. Hundreds of razor sharp glass shards screaming horizontally across entire frame. Massive bold red speed lines stretching full width. IT RAINS GLASS label in giant yellow letters thick red outline top of frame. NOT DOWN SIDEWAYS label below in bold red. 9000 KM/H in enormous bold red numbers with giant arrow. Stick figure being obliterated arms and pieces flying. Extreme dramatic energy. No white backgrounds. 9:16 vertical aspect ratio."

gen 4 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple background packed with stars. Giant swirling glass storm filling frame with infinity symbol in the centre. THE WIND HAS NEVER STOPPED label in giant red letters thick yellow outline top of frame. NOT FOR ONE SECOND label in bold yellow below. BILLIONS OF YEARS timeline arrow stretching across bottom. Stick figure tiny at bottom jaw dropped overwhelmed. Red arrows circling the storm endlessly. No white backgrounds. 9:16 vertical aspect ratio."

gen 5 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple starry background. Three blank image frames stacked with giant red X through each one. WE HAVE NEVER SEEN IT label in giant red letters thick yellow outline top of frame. NO TELESCOPE label crossed out. NO PHOTOGRAPH label crossed out. NOTHING label in enormous bold letters centre frame. Stick figure scientist with clipboard looking confused and shocked. Red arrows pointing at blank frames. No white backgrounds. 9:16 vertical aspect ratio."

gen 6 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark purple background. Stick figure scientist centre frame holding giant board showing how glass kills a stick figure. WE KNOW EXACTLY HOW IT KILLS YOU label in giant red letters thick yellow outline filling top of frame. ALL FROM A SHADOW label below in bold yellow with red arrow pointing at tiny dark shadow shape. Warning symbols everywhere. Lots of colour vivid purples electric blues warm reds. No white backgrounds. 9:16 vertical aspect ratio."

gen 7 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple starry space background packed with bright white stars. One specific star centre frame slightly dimmer than the rest with red arrow pointing directly at it. A SINGLE DIMMING label in giant yellow letters thick red outline top of frame. 63 LIGHT YEARS AWAY label in bold red below with enormous distance arrow. Stick figure squinting through telescope jaw dropped. No white backgrounds. 9:16 vertical aspect ratio."

gen 8 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple space background absolutely packed with bright white stars glowing planets and vivid nebula clouds stretching to every edge. Stick figure centre frame arms wide open head tilted back looking up overwhelmed. IF WE FOUND THIS FROM JUST A SHADOW label in giant yellow letters thick red outline top of frame. WHAT ELSE IS OUT THERE label in giant red letters below with question marks everywhere. No white backgrounds. 9:16 vertical aspect ratio."

gen 9 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple starry space background packed with bright white stars glowing planets colourful nebulas and deep sea creatures in corners. Giant glowing subscribe button centre frame. FOLLOW UNKNOWN ORIGINS in giant yellow letters thick red outline top of frame. SPACE MYSTERIES AND DEEP SEA HORRORS label in bold red below. EVERY SINGLE WEEK label in yellow. Stick figure pressing button with massive excited expression eyes huge. Speed lines radiating outward. No white backgrounds. 9:16 vertical aspect ratio."

gen 10 "Stick figure illustration with rich vibrant colourful backgrounds. Higgsfield Nano Banana Pro style. Thick uneven black outlines. Wobbly hand drawn lines. Deep dark blue purple space background absolutely packed with stars planets nebulas and the glass planet glowing ominously centre frame with shards swirling around it. Stick figure tiny at bottom looking up completely overwhelmed arms shaking. YOU ARE NOT READY label in enormous bold red letters thick yellow outline filling top third of frame. Red arrows pointing everywhere at the universe. Maximum dramatic energy speed lines radiating outward. No white backgrounds. 9:16 vertical aspect ratio."

echo ""
echo "All 10 scenes generated! Check the output_glass_short2/ folder."
