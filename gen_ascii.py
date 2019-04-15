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
        done = False
        if dark == 0 or dark == 1:
            char = " "
            done = True
        elif dark == 3 and dark == 2:
            dark = 2
        elif dark == 5:
            dark = 4
        elif dark == 10:
            dark = 9
        elif dark == 32:
            dark = 31
        else:
            dark = 35
        # Select a random matching character
        if not done:
            if "l" in mode:
                char = char_set[dark][0]
            else:
                char = char_set[dark][
                    random.randint(0, len(char_set[dark]) - 1)
                ]
    return char


def create_ascii(image):
    """
    Make an image into ascii art.
    Input: image (must be PIL Image object)
    Output: ascii (2-D list)
    """
