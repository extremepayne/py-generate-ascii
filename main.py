"""Module Docstring."""
# pylint: disable=C0103

# Imports
import os
import constants
import time

try:
    from PIL import Image
except ImportError:
    print("You need to install pillow (6.x) for this project to work.")
    print("Do this in you command line: `pip install pillow`")


LETTER_SCALE = constants.MAX_VAL - constants.MIN_VAL + 1
GRAY_SCALE = 255 - 1 + 1
SCALE = GRAY_SCALE / LETTER_SCALE

user_input = input(
    'Enter the path of your file\n\
(absolute or relative path, type "demo" for a demo)\n'
)

if user_input == "demo":
    img = Image.open("images\python-pix-sm-transparent.png")
    print(img.format, img.size)
    outpt_list = []
    to_append = []
    for column in range(img.size[0]):
        to_append.append("")
        # make a list with as many strings as there are columns
    for row in range(img.size[1]):
        outpt_list.append(to_append)
        # Nest that list into a list with as many lists as there are rows.
    print(outpt_list, len(outpt_list))
    for col in range(img.size[0]):
        for row in range(img.size[1]):
            color = img.getpixel((col, row))
            if color[3] > 0:  # If the pixel isn't transparent:
                darkness = round(
                    color[0] / SCALE
                )  # If the image is grayscale, we can
                # just assume the red component is represetative of the overall
                # brightnes of the pixel.


elif ".png" in user_input:
    assert os.path.exists(user_input), "I did not find the file at, " + str(
        user_input
    )
    img = Image.open(user_input)
    for column in range(img.size[0]):
        to_append.append("")
    for row in range(img.size[1]):
        outpt_list.append(to_append)

else:
    print("File must be a png.\n\n\n")

print("This is a work in progress.")
