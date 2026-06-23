#!/bin/bash

HF=/opt/homebrew/lib/node_modules/@higgsfield/cli/vendor/hf
STYLE="Stick figure illustration rich vibrant colours. Thick uneven black outlines. Wobbly hand drawn lines. No text no labels no writing. Deep dark blue and purple space backgrounds packed with bright white stars glowing planets and colourful nebulas. Lots of colour bright yellows electric blues vivid purples warm oranges glowing greens. No realistic shading no 3D no white backgrounds. 16:9 aspect ratio."

mkdir -p output_hestia

gen_extra() {
  local num=$1
  local scene=$2
  echo "Generating $num..."
  local job_id=$($HF generate create nano_banana_2 --prompt "$STYLE $scene" --json 2>/dev/null | tr -d '[]" \n')
  if [[ -n "$job_id" ]]; then
    $HF generate wait "$job_id" > "output_hestia/image_${num}.txt" 2>&1
    echo "Done $num"
  else
    echo "FAILED $num"
  fi
}

gen_extra 121 "glowing green planet with rings floating in deep purple starry space"
gen_extra 122 "orange dwarf star radiating warm golden light surrounded by planets and stars"
gen_extra 123 "shallow turquoise ocean under a purple sky with two moons glowing above"
gen_extra 124 "dense tropical jungle on an alien planet with giant colourful plants and bright sun"
gen_extra 125 "asteroid field floating in deep space with colourful nebula clouds behind"
gen_extra 126 "stick figure astronaut floating in space looking at a massive glowing planet"
gen_extra 127 "distant galaxy spiral glowing in deep purple and blue space full of stars"
gen_extra 128 "alien planet surface with glowing volcanic mountains and bright starry sky"
gen_extra 129 "two planets side by side glowing in deep space one blue one orange surrounded by stars"
gen_extra 130 "stick figure standing on a small planet looking up at an enormous glowing star filling the sky"

echo ""
echo "All 10 extra images generated!"
