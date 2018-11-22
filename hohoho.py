from sys import argv
from whitespace.cli import main

# Take in a file
file_name = argv[-1]  # Assume for now it's just the last one

with open(file_name) as input_file:
    lines = input_file.readlines()

# Converts 'hohoho' to \t
# Converts ' ' to ''
# Converts 'ho' to ' '

for i in range(len(lines)):
    lines[i] = lines[i].replace("hohoho", "\t")
    lines[i] = lines[i].replace(" ", "")
    lines[i] = lines[i].replace("ho", " ")

# Write to temp file

# Run temp file with whitespace thingy

# Delete tmp file

# Done
# main([file_name])
