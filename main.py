"""Module Docstring."""

import constants

try:
    import PIL
except ImportError:
    print("You need to install pillow for this project to work.")
    print("Do this in you command line: `pip install pillow`")


print(constants.CHAR_DARKNESS)

print("This is a work in progress.")
