"""Module Docstring."""
# pylint: disable=C0103

import os
import constants


try:
    from PIL import Image
except ImportError:
    print("You need to install pillow (6.x) for this project to work.")
    print("Do this in you command line: `pip install pillow`")


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
    for row in range(img.size[1]):
        outpt_list.append(to_append)
    print(outpt_list, len(outpt_list))

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
