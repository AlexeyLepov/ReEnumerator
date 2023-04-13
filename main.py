# define custom opening and closing brackets for id
id_opening_bracket = "\""
id_closing_bracket = "\""
# define custom lines separator
lines_separator = ","
# initialize line counter
i = 0
# initialize output lines list
output_lines = []  


##############################
#                            #
#    open your input file    #
#                            #
##############################
with open('file_input.txt', 'r') as f:
    lines = f.readlines()


#################################
#                               #
#    parse lines - main loop    #
#                               #
#################################
for line in lines:
    # process comments
    if line.startswith("#"):
        # add comment to output lines 
        # "rstrip()" removes the line break character (writes your comment without extra line break after it)
        output_lines.append(line.rstrip())
    # process non-comment lines
    else:
        # split line by comma
        line = line.strip().split(lines_separator)
        # re-enumerate the first value
        line[0] = id_opening_bracket + f"{i+1:04}" + id_closing_bracket
        # join the modified values with comma
        line = lines_separator.join(line)
        # add modified line to output lines
        output_lines.append(line)
        i += 1


########################################
#                                      #
#    write data to your output file    #
#                                      #
########################################
with open('file_output.txt', 'w') as f:
    # add line break at the end of the file
    f.write('\n'.join(output_lines) + '\n')
    