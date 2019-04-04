"""Module Docstring."""
# pylint: disable=C0103

import os
import constants


try:
    from PIL import Image
except ImportError:
    print("You need to install pillow (6.x) for this project to work.")
    print("Do this in you command line: `pip install pillow`")


user_input = input("Enter the path of your file (absolute or relative): ")
if user_input == "demo":
    img = Image.open("images\python-pix-sm-transparent.png")
    print(img.format, img.size)
elif ".png" in user_input:
    assert os.path.exists(user_input), "I did not find the file at, " + str(
        user_input
    )
    img = Image.open(user_input)
    print(img.format, img.size)
else:
    print("File must be a png.\n\n\n")

print("This is a work in progress.")
