# RedHat
A script that receive an input (file, files or just a stdin) and regular expression, and return the regex matches

## basic syntax:
line_searcher.py -r <--regex> [[[[-f <--files>] -u] -c] -m]")
- -r, --regex     mandatory - the regular expression to search for.")
- -f, --files     optional  - a string or path to directory or file to search in.
                              If this parameter is omitted, the script expects text input from STDIN.
- -u, --underline optional  - "^" is printed underneath the matched text.
- -c, --color     optional  - the matched text is highlighted in color - RED, PURPLE, BLUE, JADE, GREEN and YELLOW
- -m, --machine   optional  - print the output in the format: "file_name:line_number:start_position:matched_text"

## Examples:
1. **line_searcher.py -r "nir" -f "sssnirgggg"** -
This command will search the regex in the given string

2. **line_searcher.py -r "nir" -f "input/"** -  
This command will search the regex in the given directory files

3. **line_searcher.py -r "nir" -f "input/input1.txt"** - This command will search the regex in the given file

4. **line_searcher.py -r "nir"** - This command will search the regex in entered STDIN ('enter' for a new line, ctrl+d to end)

5. **line_searcher.py -r "nir" -u -c BLUE -m ** - This command will search the regex in entered STDIN, colored the findings with blue, add underline with ^^ and prints the results on vm syntax
