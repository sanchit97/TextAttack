def has_letter(word):
    """ Returns true if `word` contains at least one character in [A-Za-z]. """
    for c in word:
        if c.isalpha():
            return True
    return False


def add_indent(s_, numSpaces):
    s = s_.split("\n")
    # don't do anything for single-line stuff
    if len(s) == 1:
        return s_
    first = s.pop(0)
    s = [(numSpaces * " ") + line for line in s]
    s = "\n".join(s)
    s = first + "\n" + s
    return s


def words_from_text(s, words_to_ignore=[], words2char=False):
    """ Lowercases a string, removes all non-alphanumeric characters,
        and splits into words. """
    words = []
    words2char_offset = {}
    word = ""
    start = 0
    end = 0
    for i, c in enumerate(s):
        if c.isalpha():
            word += c
            if start < end:
                start = i
        elif word:
            if word not in words_to_ignore:
                words.append(word)
                end = i - 1
                words2char_offset[word] = (start, end)
            word = ""
    if len(word) and (word not in words_to_ignore):
        words.append(word)
        end = len(word) - 1
        words2char_offset[word] = (start, end)
    
    if words2char:
        return words, words2char_offset
    else:
        return words


def default_class_repr(self):
    extra_params = []
    for key in self.extra_repr_keys():
        extra_params.append("  (" + key + ")" + ":  {" + key + "}")
    if len(extra_params):
        extra_str = "\n" + "\n".join(extra_params) + "\n"
        extra_str = f"({extra_str})"
    else:
        extra_str = ""
    extra_str = extra_str.format(**self.__dict__)
    return f"{self.__class__.__name__}{extra_str}"


LABEL_COLORS = [
    "red",
    "green",
    "blue",
    "purple",
    "yellow",
    "orange",
    "pink",
    "cyan",
    "gray",
    "brown",
]


def color_from_label(label_num):
    """ Arbitrary colors for different labels. """
    try:
        label_num %= len(LABEL_COLORS)
        return LABEL_COLORS[label_num]
    except TypeError:
        return "purple"


class ANSI_ESCAPE_CODES:
    """ Escape codes for printing color to the terminal. """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    GRAY = "\033[37m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    """ This color stops the current color sequence. """
    STOP = "\033[0m"


def color_text(text, color=None, method=None):
    if not (isinstance(color, str) or isinstance(color, tuple)):
        raise TypeError(f"Cannot color text with provided color of type {type(color)}")
    if isinstance(color, tuple):
        if len(color) > 1:
            text = color_text(text, color[1:], method)
        color = color[0]

    if method is None:
        return text
    if method == "html":
        return f"<font color = {color}>{text}</font>"
    elif method == "ansi":
        if color == "green":
            color = ANSI_ESCAPE_CODES.OKGREEN
        elif color == "red":
            color = ANSI_ESCAPE_CODES.FAIL
        elif color == "blue":
            color = ANSI_ESCAPE_CODES.OKBLUE
        elif color == "gray":
            color = ANSI_ESCAPE_CODES.GRAY
        elif color == "bold":
            color = ANSI_ESCAPE_CODES.BOLD
        elif color == "underline":
            color = ANSI_ESCAPE_CODES.UNDERLINE
        elif color == "warning":
            color = ANSI_ESCAPE_CODES.WARNING
        else:
            raise ValueError(f"unknown text color {color}")

        return color + text + ANSI_ESCAPE_CODES.STOP
    elif method == "file":
        return "[[" + text + "]]"
