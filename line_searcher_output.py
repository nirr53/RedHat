import re
import os


class line_searcher_output():

    def __init__(self, _regex, _stdin_prefix, _is_underline, _is_color, _is_machine):
        self.regex = _regex
        self.stdin_prefix = _stdin_prefix
        self.is_underline = _is_underline
        self.is_color = _is_color
        self.is_machine = _is_machine
        self.PURPLE = '\033[95m'
        self.BLUE   = '\033[94m'
        self.JADE   = '\033[96m'
        self.GREEN  = '\033[92m'
        self.YELLOW = '\033[93m'
        self.RED    = '\033[91m'
        self.TEXT   = '\033[0m'

    def searh_and_print(self, is_files, data):
        matches_list = []
        is_file = True if os.path.isfile(is_files) else False
        is_dir  = True if os.path.isdir(is_files) else False
        if is_files and (is_file or is_dir):
            for _file in data:
                if is_file:
                    full_path = _file
                else:
                    full_path = is_files + _file
                with open(full_path) as _file_handle:
                    lines = _file_handle.readlines()
                matches_list = self.search_regexp(lines, matches_list, _file)
        else:
            matches_list = self.search_regexp(data, matches_list, self.stdin_prefix)
        self.print_results(matches_list)

    def print_results(self, matches):
        if self.is_machine:
            for match in matches:
                if self.is_color:
                    wrapped_line = self.add_color(match[2])
                    print("{}:{}:{}:{}".format(match[0], match[1], match[3], wrapped_line))
                else:
                    print("{}:{}:{}:{}".format(match[0], match[1], match[3], match[2]))
                if self.is_underline:
                    fixed_line = self.create_underlined_line(match)
                    print(fixed_line)
        else:
            for match in matches:
                if self.is_color:
                    wrapped_line = self.add_color(match[2])
                    print("{} {} {}".format(match[0], match[1], wrapped_line))
                else:
                    print("{} {} {}".format(match[0], match[1], match[2]))
                if self.is_underline:
                    fixed_line = self.create_underlined_line(match)
                    print(fixed_line)

    def create_underlined_line(self, match):
        occ_idx_array = [m.start() for m in re.finditer(self.regex, match[2])]
        regex_underlines_str_len = len(self.regex)
        regex_underlines_str     = "^" * regex_underlines_str_len
        fixed_line               = " " * (len(match[0]) + len(str(match[1])) + 2)
        line_length              = len(match[2])
        occ_idx, idx = 0, 0
        while idx < line_length:
            if idx == occ_idx_array[occ_idx]:
                fixed_line += regex_underlines_str
                idx += regex_underlines_str_len
                if (occ_idx + 1) < len(occ_idx_array):
                    occ_idx += 1
            else:
                fixed_line += " "
                idx += 1

        return fixed_line

    def add_color(self, line):
        color = self.get_color(self.is_color)
        count = line.count(self.regex)
        for idx in range(count):
            if self.is_machine:
                line = color + line + self.TEXT
            else:
                start_idx = [m.start() for m in re.finditer(self.regex, line)]
                end_idx = [m.end() for m in re.finditer(self.regex, line)]
                start, end = start_idx[idx], end_idx[idx]
                line = line[:start] + color + self.regex + self.TEXT + line[end:]
        return line

    def get_color(self, _color):
        if "PURPLE" in _color:
            return self.PURPLE
        elif "BLUE" in _color:
            return self.BLUE
        elif "JADE" in _color:
            return self.JADE
        elif "GREEN" in _color:
            return self.GREEN
        elif "YELLOW" in _color:
            return self.YELLOW
        elif "RED" in _color:
            return self.RED

    def search_regexp(self, lines, matches_list, filename, file_line_num=1):
        for line in lines:
            if self.regex in line:
                if self.is_machine:
                    words = line.split()
                    _temp_line = ""
                    for word in words:
                        if re.search(self.regex, word):
                            _temp_line += word + " "
                    matches_list.append([filename, file_line_num, _temp_line, line.find(self.regex)])
                else:
                    matches_list.append([filename, file_line_num, line.rstrip()])
            file_line_num += 1
        return matches_list
