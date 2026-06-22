#!/bin/bash

# Downloads all generated images as JPEGs to a folder on your Desktop
# Run this AFTER generate_images.sh has finished

OUTPUT_DIR="$HOME/Desktop/test-project-/output"
IMAGES_DIR="$HOME/Desktop/space_images"

mkdir -p "$IMAGES_DIR"

echo "Downloading images..."

for txt_file in "$OUTPUT_DIR"/image_*.txt; do
  num=$(basename "$txt_file" | grep -o '[0-9]*')
  url=$(cat "$txt_file" | tr -d '\n' | tr -d ' ')

  if [[ "$url" == http* ]]; then
    echo "Downloading image $num..."
    curl -s -o "$IMAGES_DIR/image_${num}.jpeg" "$url"
    echo "Done $num"
  else
    echo "Skipping $num (no URL yet)"
  fi
done

echo ""
echo "All done! Images saved to: $IMAGES_DIR"
open "$IMAGES_DIR"
