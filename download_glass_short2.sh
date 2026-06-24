#!/bin/bash

OUTPUT_DIR="$HOME/Desktop/test-project-/output_glass_short2"
IMAGES_DIR="$HOME/Movies/glass_short2"

mkdir -p "$IMAGES_DIR"

echo "Downloading glass short 2 scenes..."

for i in $(seq 1 10); do
  txt_file="$OUTPUT_DIR/image_${i}.txt"
  num=$(printf "%02d" $i)
  filename="short2_scene${num}.jpeg"

  if [ ! -f "$txt_file" ]; then
    echo "Skipping $i (no file)"
    continue
  fi

  url=$(grep -o 'https://[^ ]*\.jpeg\|https://[^ ]*\.png\|https://[^ ]*\.jpg' "$txt_file" | head -1)

  if [[ -n "$url" ]]; then
    echo "Downloading scene $i as $filename..."
    curl -s -o "$IMAGES_DIR/$filename" "$url"
    echo "Done $i"
  else
    echo "Skipping $i (no URL found)"
  fi
done

echo ""
echo "All done! Images saved to: $IMAGES_DIR"
open "$IMAGES_DIR"
