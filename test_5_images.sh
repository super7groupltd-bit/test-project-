#!/bin/bash

# Test script - first 5 scenes from the script

STYLE="Hand-drawn stick figure illustration style inspired by the YouTube channel Zenn. Simple stick figures with round heads, dot eyes, and expressive body language. Rich vibrant colourful backgrounds — space scenes have deep dark blue and purple backgrounds packed with bright white stars, glowing yellow suns, blue and green Earth, orange and red planets, silver rockets and space stations. Lots of colour — bright yellows, electric blues, vivid purples, warm oranges, glowing greens. Bold black outlines on all figures and objects. Wobbly hand-drawn feel but colourful and lively. Red arrows and handwritten labels for emphasis. Every scene feels alive with colour and energy. Not realistic, not 3D, not photographic. Charming, expressive and packed with colour."

mkdir -p test_output

gen() {
  local num=$1
  local prompt=$2
  echo "Generating test image $num..."
  higgsfield generate create nano_banana_2 --prompt "${STYLE} ${prompt}" --aspect-ratio 16:9 --wait > "test_output/test_${num}.txt" 2>&1
  echo "Done $num - check test_output/test_${num}.txt for URL"
}

gen 1 "A stick figure person lying in bed under a wobbly blanket, eyes closed with ZZZ floating above. A light switch on the wall with a red arrow. Simple moon and stars outside a lopsided window."

gen 2 "A stick figure lying in bed. A thought bubble above their head that is completely empty. Wobbly lines."

gen 3 "A wonky circle Earth at the bottom. A tiny boxy space station above it. Dotted line showing distance labelled 408KM in handwriting. Six tiny stick figures visible inside the station."

gen 4 "A stick figure astronaut floating inside a box with question marks all around their head. Small porthole window with scribbled stars outside. Confused expression."

gen 5 "Split drawing. Left side: moon and dark sky labelled NIGHT. Right side: big yellow blazing sun labelled ALSO NOW with a red arrow. Stick figure astronaut looking baffled in the middle."

echo ""
echo "All 5 test images done! Open test_output folder and paste URLs into your browser to check the style."
open test_output
