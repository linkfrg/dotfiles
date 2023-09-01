#!/bin/bash

# Set the directory path
dir_path="$HOME/.wallpaper"

# Find image files (adjust the extensions as needed)
image_files=$(find "$dir_path" -type f \( -iname \*.jpg -o -iname \*.jpeg -o -iname \*.png -o -iname \*.gif \))

# Convert the list of image files to JSON format
json_array="["
for file in $image_files; do
    if [ "$json_array" != "[" ]; then
        json_array+=","  # Add comma separator between array elements
    fi
    json_array+="\"$file\""
done
json_array+="]"

# Print the JSON array
echo "$json_array"
