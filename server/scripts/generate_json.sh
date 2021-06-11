#!/bin/bash

# usage: bash script.sh /path/to/pics /path/to/output/json

for img in "$1"/*.jpg "$1"/*.jpeg; do
	name=$(echo "$img" | cut -f 6 -d '/')
	json="$(echo "$name" | cut -f 1 -d '.' ).json"
	folder="$(echo "$img" | cut -f 5 -d '/' )"
	new_file="server/shared/json/Tripix/$json"

	if ! [ -d "server/shared/json/$folder" ]; then 
	    mkdir "server/shared/json/$folder"
	fi

	printf "{\n" > "$new_file";
	printf "  \"dataset\": \"Tripix\",\n" >> "$new_file";
	printf "  \"url\": \"%s\",\n" "$img" >> "$new_file";
	printf "  \"labels\": {},\n" >> "$new_file";
	printf "  \"text\": \"%s\",\n" "$folder" >> "$new_file";
	printf "  \"text_url\": \"%s\"\n" "$folder" >> "$new_file";		
	printf "}\n" >> "$new_file";
done
