# define custom opening and closing brackets for id
id_opening_bracket = "\""
id_closing_bracket = "\""
lines_separator = ","

with open('file_input.txt', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line = line.strip().split(lines_separator)  # split line by comma
    line[0] = id_opening_bracket + f"{i+1:04}" + id_closing_bracket  # re-enumerate the first value
    line = lines_separator.join(line)  # join the modified values with comma
    lines[i] = line

with open('file_output.txt', 'w') as f:
    f.write('\n'.join(lines))