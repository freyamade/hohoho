import os
from whitespace.cli import main

def boobooboo_to_whitespace(file_name):
    with open(file_name) as input_file:
        lines = input_file.readlines()

    # Converts 'hohoho' to \t
    # Converts ' ' to ''
    # Converts 'snow' to ' '
    for i in range(len(lines)):
        lines[i] = lines[i].replace('boobooboo', '\t')
        lines[i] = lines[i].replace(' ', '')
        lines[i] = lines[i].replace('spoopy', ' ')

    # Write the transpiled lines to a temp file and interpret that using the whitespace interpreter
    with open('output.ws', 'w') as f:
        for line in lines:
            f.write(line)
    main(['output.ws'])
    os.remove('output.ws')
