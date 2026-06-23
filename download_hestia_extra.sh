#!/bin/bash

OUTPUT_DIR="$HOME/Desktop/test-project-/output_hestia"
IMAGES_DIR="$HOME/Movies/video_hestia"

mkdir -p "$IMAGES_DIR"

echo "Downloading extra images..."

for i in 121 122 123 124 125 126 127 128 129 130; do
  txt_file="$OUTPUT_DIR/image_${i}.txt"

  if [ ! -f "$txt_file" ]; then
    echo "Skipping $i (no file)"
    continue
  fi

  url=$(grep -o 'https://[^ ]*\.jpeg\|https://[^ ]*\.png\|https://[^ ]*\.jpg' "$txt_file" | head -1)

  if [[ -n "$url" ]]; then
    echo "Downloading image $i..."
    curl -s -o "$IMAGES_DIR/extra_${i}.jpeg" "$url"
    echo "Done $i"
  else
    echo "Skipping $i (no URL found)"
  fi
done

echo ""
echo "All done! Images saved to: $IMAGES_DIR"
open "$IMAGES_DIR"
