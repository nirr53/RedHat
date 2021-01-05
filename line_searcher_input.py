import getopt
import sys
import os


class line_searcher_input():

    def __init__(self):
        pass

    def filter_argv(self):
        _regex, _files, _is_color = None, None, None
        _is_underline, _is_machine_printed = False, False
        optlist, args = getopt.getopt(sys.argv[1:], 'r:f:uc:mh')
        for opt, arg in optlist:
            if "-r" in opt:
                _regex = arg
            elif "-f" in opt:
                _files = arg
            elif "-u" in opt:
                _is_underline = True
            elif "-c" in opt:
                if arg in ["RED", "PURPLE", "BLUE", "JADE", "GREEN", "YELLOW"]:
                    _is_color = arg
                else:
                    print("\tUnknown color was detected !")
                    print("\tThe supported colors are: RED, PURPLE, BLUE, JADE, GREEN and YELLOW")
                    exit(sys.exit(2))
            elif "-m" in opt:
                _is_machine_printed = True
            elif "-h" in opt:
                self.print_help()
                exit(sys.exit(0))
            else:
                print("Unknown attribute was detected ! The format is:")
                print("  line_searcher.py -r <--regex> [[[[-f <--files>] -u] -c] -m]")
                exit(sys.exit(2))
        if not _regex:
            print("The -r (--regex) attribute was not detected !")
            exit(sys.exit(2))
        return _regex, _files, _is_underline, _is_color, _is_machine_printed

    def read_stdin_input(self, _files, data=[]):
        if not _files:
            while True:
                line = sys.stdin.readline()
                if line == '':
                    break
                data.append(line)
        else:
            if os.path.isdir(_files):
                for filename in os.listdir(_files):
                    data.append(filename)
            elif os.path.isfile(_files):
                data.append(_files)
            else:
                if isinstance(_files, str):
                    data.append(_files)
                else:
                    print("The input path <{}> is invalid !".format(_files))
                    exit(sys.exit(2))
        return data

    def print_help(self):
            print("\n\t------------------ H E L P -----------------\n")
            print("\tline_searcher.py -r <--regex> [[[[-f <--files>] -u] -c] -m]")
            print("\t-r, --regex     mandatory - the regular expression to search for.")
            print("\t-f, --files     optional  - a list of files to search in.")
            print("\t                If this parameter is omitted, the script expects text input from STDIN.")
            print("\t-u, --underline optional  - \"^\" is printed underneath the matched text.")
            print("\t-c, --color     optional  - the matched text is highlighted in color - RED, PURPLE, BLUE, JADE, GREEN and YELLOW")
            print("\t-m, --machine   optional  - print the output in the format: \"file_name:line_number:start_position:matched_text\".\n")
