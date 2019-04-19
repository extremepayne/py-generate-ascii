"""Importable; generate ascii art from image."""


def generate_char(dark, mode, char_set):
    """Select a courier character based on a darkness level."""
    import random

    if len(char_set[dark]) > 0:
        # Select a random matching character
        if "l" in mode:
            char = char_set[dark][0]
        else:
            char = char_set[dark][random.randint(0, len(char_set[dark]) - 1)]
    else:
        # Some darknesses aren't covered by
        # the avaliable characters
        if dark in (0, 1):
            char = " "
            return char
        else:
            i = 1
            done = False
            while not done:
                if len(char_set[dark + i]) > 0:
                    new_dark = dark + i
                    done = True
                elif len(char_set[dark - i]) > 0:
                    new_dark = dark - i
                    done = True
                i += 1
        # Select a random matching character
        if "l" in mode:
            char = char_set[new_dark][0]
        else:
            char = char_set[new_dark][
                random.randint(0, len(char_set[new_dark]) - 1)
            ]
    return char


def get_char_set(char_dict, max_val):
    """Generate a list of characters from a dictionary."""
    char_set = []
    i = 0
    while i < max_val + 1:
        char_set.append([])
        i += 1
    for letter, thickness in char_dict.items():
        char_set[thickness].append(letter)
    return char_set


def create_ascii(image):
    """
    Make an image into ascii art.
    Input: image (must be PIL Image object)
    Output: ascii (2-D list)
    """
