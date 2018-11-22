from sys import argv
from tempfile import NamedTemporaryFile
from whitespace.cli import main

# Take in a file
file_name = argv[-1]  # Assume for now it's just the last one

with open(file_name) as input_file:
    lines = input_file.readlines()

# Convert `ho` to space
# Convert `hohoho` to \t
# Convert \n to \n
# Read the file line by line
# Replace hohoho with \t and ho with ' '
# Replace ' ' with ''


# Write the transpiled lines to a temp file and interpret that using the whitespace interpreter
with NamedTemporaryFile() as temp_file:
    for line in lines:
        temp_file.write()
    main([temp_file.name])
