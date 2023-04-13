#################################################################
#                                                               #
#    this module deletes empty lines in your input text file    #
#                                                               #
#################################################################

# Open the input file for reading and the output file for writing
with open('file_input.txt', 'r') as input_file, open('file_output.txt', 'w') as output_file:
    # Loop over each line in the input file
    for line in input_file:
        # If the line is not empty, write it to the output file
        if line.strip():
            output_file.write(line)