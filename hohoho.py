from sys import argv
from whitespace.cli import main

# Take in a file
file_name = argv[-1]  # Assume for now it's just the last one

with open(file_name) as input_file:
    lines = input_file.readlines()

print(lines)
# Convert `ho` to space
# Convert `hohoho` to \t
# Convert \n to \n
# Read the file line by line
# Replace hohoho with \t and ho with ' '
# Replace ' ' with ''


# Write to temp file

# Run temp file with whitespace thingy

# Delete tmp file

# Done
# main([file_name])
