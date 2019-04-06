"""Module Docstring."""
# pylint: disable=C0103

# Imports
import os
import random
import constants
import time

try:
    from PIL import Image
except ImportError:
    print("You need to install pillow (6.x) for this project to work.")
    print("Do this in you command line: `pip install pillow`")
    input("Press enter to continue")
    quit()


LETTER_SCALE = constants.MAX_VAL - constants.MIN_VAL + 1
GRAY_SCALE = 255 - 1 + 1
SCALE = GRAY_SCALE / LETTER_SCALE

CHARS = []
for i in range(constants.MAX_VAL + 1):
    CHARS.append([])
for letter, thickness in constants.CHAR_DARKNESS.items():
    CHARS[thickness].append(letter)
i = 0
for item in CHARS:
    if len(item) == 0:
        print(i)
    i += 1

user_input = input(
    'Enter the path of your file\n\
(absolute or relative path, type "demo" for a demo)\n'
)

if user_input == "demo":
    img = Image.open("images\python-pix-sm-transparent.png")
    print(img.format, img.size)
    output_list = []
    to_append = []
    for column in range(img.size[0]):
        to_append.append("")
        # make a list with as many strings as there are columns.
    for row in range(img.size[1]):
        output_list.append(to_append)
        # Nest that list into a list with as many lists as there are rows.
    for col in range(img.size[0]):
        for row in range(img.size[1]):
            color = img.getpixel((col, row))
            print(color)
            if color[3] > 0:  # If the pixel isn't transparent:
                darkness = (
                    round(color[0] / SCALE) + 1
                )  # If the image is grayscale, we can
                # just assume the red component is represetative of the overall
                # brightnes of the pixel.
                if len(CHARS[darkness]) > 0:
                    char = CHARS[darkness][
                        random.randint(0, len(CHARS[darkness]) - 1)
                    ]
                else:
                    # Some darknesses aren't covered by
                    # the avaliable characters
                    if darkness <= 3:
                        darkness = 2
                    elif darkness == 5:
                        darkness = 4
                    elif darkness == 10:
                        darkness = 9
                    elif darkness == 32:
                        darkness = 31
                    else:
                        darkness = 35
                    char = CHARS[darkness][
                        random.randint(0, len(CHARS[darkness]) - 1)
                    ]
            elif color[3] == 0:
                char = " "
            output_list[row][col] = char

    print(output_list)


elif ".png" in user_input:
    assert os.path.exists(user_input), "I did not find the file at, " + str(
        user_input
    )
    img = Image.open(user_input)
    for column in range(img.size[0]):
        to_append.append("")
    for row in range(img.size[1]):
        output_list.append(to_append)

else:
    print("File must be a png.\n\n\n")

print("This is a work in progress.")
