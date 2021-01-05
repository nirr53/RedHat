from line_searcher_input import line_searcher_input
from line_searcher_output import line_searcher_output

# input data
in_parser = line_searcher_input()
stdin_prefix = "stdin"

# parse the command line
_regex, _files, _is_underline, _is_color, _is_machine_printed = in_parser.filter_argv()
out_searcher = line_searcher_output(_regex,
                                    stdin_prefix,
                                    _is_underline,
                                    _is_color,
                                    _is_machine_printed)

# get a list of input file/s or the stdin lines
data = in_parser.read_stdin_input(_files)

# Search the regex in the given data, and print it according the supported flags
out_searcher.searh_and_print(_files, data)

# todo debuging