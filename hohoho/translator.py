def whitespace_to_boobooboo(input_file_name,output_file_name):
    with open(input_file_name) as input_file:
        lines = input_file.readlines()

    # Converts 'boobooboo' to \t
    # Converts ' ' to ''
    # Converts 'boo' to ' '
    for i in range(len(lines)):
        lines[i] = lines[i].replace(' ', 'spoopy ')
        lines[i] = lines[i].replace('\t', 'boobooboo ')


    # Write the transpiled lines to a temp file and interpret that using the whitespace interpreter
    with open(output_file_name, 'w') as f:
        for line in lines:
            f.write(line)
