#!/bin/bash

OUTPUT_DIR="$HOME/Desktop/test-project-/output_glass_short"
IMAGES_DIR="$HOME/Movies/glass_short"

mkdir -p "$IMAGES_DIR"

echo "Downloading glass short scenes..."

FILENAMES=(
  "short1_scene01"
  "short1_scene02"
  "short1_scene03"
  "short1_scene04"
  "short1_scene05"
  "short1_scene06"
  "short1_scene07"
  "short1_scene08"
  "short1_scene09"
  "short1_scene10"
)

for i in $(seq 1 10); do
  num=$(printf "%02d" $i)
  txt_file="$OUTPUT_DIR/image_${i}.txt"
  filename="${FILENAMES[$((i-1))]}.jpeg"

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
