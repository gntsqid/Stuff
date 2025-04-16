#!/bin/bash

# NOTE: Needs to be a cron job and assumes credential store

# Start from the home directory
start_directory="$HOME"

# Find all .git directories recursively
find "$start_directory" -type d -name ".git" | while read -r gitdir; do
    # Move to the parent directory of each .git folder
    repo_dir=$(dirname "$gitdir")
    #echo "Entering repository: $repo_dir"
    cd "$repo_dir" || continue

    # Execute git pull
    #echo "Running 'git pull' in $repo_dir"
    git pull 2>/dev/null

    # Navigate back to the start directory
    cd "$start_directory" || exit
done
