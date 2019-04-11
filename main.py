"""Module Docstring."""
# pylint: disable=C0103

# Imports
import os
import random
import platform
import constants  # Local; has some variable I didn't want cluttering this file

# PIL used to process images
try:
    from PIL import Image
except ImportError:
    print("You need to install pillow (6.x) for this project to work.")
    print("Do this in you command line: `pip install pillow`")
    input("Press enter to continue")
    quit()


# Find the scalar variable used to convert from rgb to courier
LETTER_SCALE = constants.MAX_VAL - constants.MIN_VAL + 1
GRAY_SCALE = 255 - 1 + 1
SCALE = GRAY_SCALE / LETTER_SCALE

# Extract the data from constants into a useable form
CHARS = []
for i in range(constants.MAX_VAL + 1):
    CHARS.append([])
for letter, thickness in constants.CHAR_DARKNESS.items():
    CHARS[thickness].append(letter)
i = 0


def generate_char(dark):
    if len(CHARS[dark]) > 0:
        # Select a random matching character
        char = CHARS[dark][random.randint(0, len(CHARS[dark]) - 1)]
    else:
        # Some darkes aren't covered by
        # the avaliable characters
        if dark <= 3:
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
        char = CHARS[dark][random.randint(0, len(CHARS[dark]) - 1)]
    return char


# for item in CHARS:
# if len(item) == 0:
# print(i)
# i += 1 # This prints all darknesses without a matching character.

# User inputs the path for the file:
user_input = input(
    'Enter the path of your file\n\
(absolute or relative path, type "demo" for a demo)\n'
)

# Demo using included images:
if user_input == "demo":
    # Adjust path based on OS
    my_os = platform.system()
    if my_os == "Windows":
        img = Image.open("images\python-pix-sm-transparent.png")
    else:
        img = Image.open("images/python-pix-sm-transparent.png")
    # Print out some semi-useful info
    print(img.format, img.size)
    # Generate a 2-d list to hold output
    output_list = [[" "] * img.size[0] for _ in range(img.size[1])]
    # Loop through the image by pixels
    for row in range(img.size[1]):
        for col in range(img.size[0]):
            # grab the color of the current pixel
            color = img.getpixel((col, row))
            if color[3] > 0:  # If the pixel isn't transparent:
                darkness = (
                    round((255 - color[0]) / SCALE) + 1
                )  # If the image is grayscale, we can
                # just assume the red component is represetative of the overall
                # brightnes of the pixel.
                character = generate_char(darkness)
                output_list[row][col] = character

    # Print the output
    print("\n".join(map("".join, output_list)))
    print("You must view this in courier for the image to work.")
    # And save it to a file
    file = open("output.txt", "w")

    file.write("\n".join(map("".join, output_list)))

    file.close()
    print("The output has been saved to output.txt")


elif ".png" in user_input:
    if os.path.exists(user_input):
        img = Image.open(user_input)
        # Print out some semi-useful info
        print(img.format, img.size)
        # Generate a 2-d list to hold output
        output_list = [[" "] * img.size[0] for _ in range(img.size[1])]
        # Loop through the image by pixels
        for row in range(img.size[1]):
            for col in range(img.size[0]):
                # grab the color of the current pixel
                color = img.getpixel((col, row))
                if color[3] > 0:  # If the pixel isn't transparent:
                    darkness = (
                        round((255 - color[0]) / SCALE) + 1
                    )  # If the image is grayscale, we can
                    # just assume the red component is represetative of the overall
                    # brightnes of the pixel.
                    character = generate_char(darkness)
                    output_list[row][col] = character

        # Print the output
        print("\n".join(map("".join, output_list)))
        print("You must view this in courier for the image to work.")
        # And save it to a file
        file = open("output.txt", "w")

        file.write("\n".join(map("".join, output_list)))

        file.close()
        print("The output has been saved to output.txt")
    else:
        print("That path does not exist.")

else:
    print("File must be a png.\n\n\n")

# Wait for user before exiting.
input("Press enter to exit.")
