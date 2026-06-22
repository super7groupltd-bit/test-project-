#!/bin/bash

# Test script - 5 images to check style before running all 173

STYLE="Professional hand-drawn explainer illustration style. Colourful backgrounds relevant to the scene — deep space scenes have dark blue or black backgrounds with stars, planets, moons and rockets drawn simply but clearly. Earth scenes have warm colourful backgrounds. Bold confident black outlines. Simple stick figures with round heads, dot eyes, and expressive body language. Flat bright colours throughout — yellow suns, blue Earth, red rockets, orange and purple planets, white stars. Clear bold handwritten-style labels. Red arrows for emphasis. Simple iconic recognisable objects. Think Kurzgesagt simplified style but with stick figures. Charming, colourful, clear and expressive. Not realistic, not 3D, not photographic."

mkdir -p test_output

gen() {
  local num=$1
  local prompt=$2
  echo "Generating test image $num..."
  higgsfield generate create nano_banana_pro --prompt "${STYLE} ${prompt}" --aspect-ratio 16:9 --wait > "test_output/test_${num}.txt" 2>&1
  echo "Done $num - check test_output/test_${num}.txt for URL"
}

gen 1 "A stick figure person lying in bed under a wobbly blanket, eyes closed with ZZZ floating above. Dark blue night sky outside the window with a yellow moon and white stars."

gen 2 "A wonky blue Earth circle at the bottom of the image. A tiny boxy silver space station above it connected by a dotted line. Six tiny stick figures visible inside the station. Black starry space background with orange and purple planets visible."

gen 3 "A stick figure astronaut floating inside a space station cabin. Question marks all around their head. A small round porthole window showing black space and stars outside. Colourful interior with simple drawn equipment on walls."

gen 4 "16 tiny yellow suns and moons alternating in a circle around a boxy space station. A stick figure astronaut in the centre looking shocked with wide eyes. Dark space background full of stars."

gen 5 "A stick figure astronaut floating in front of a large dome window looking down at a glowing blue and green Earth below. Dark space background with stars and a distant moon. The astronaut has a peaceful expression."

echo ""
echo "All 5 test images done! Open test_output folder and paste URLs into your browser to check the style."
open test_output
