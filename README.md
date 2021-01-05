# RedHat
A script that receive an input (file, files or just a stdin) and regular expression, and return the regex matches

# basic syntax#
line_searcher.py -r <--regex> [[[[-f <--files>] -u] -c] -m]")
-r, --regex     mandatory - the regular expression to search for.")
-f, --files     optional  - a string or path to directory or file to search in.")
                            If this parameter is omitted, the script expects text input from STDIN.
-u, --underline optional  - "^" is printed underneath the matched text.
-c, --color     optional  - the matched text is highlighted in color - RED, PURPLE, BLUE, JADE, GREEN and YELLOW
-m, --machine   optional  - print the output in the format: "file_name:line_number:start_position:matched_text"
