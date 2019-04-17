"""Generate ascii art from image."""
# pylint: disable=C0103

# Imports
import os
import random
import platform
import statistics
import constants  # Local; has some variable I didn't want cluttering this file

# PIL used to process images
try:
    from PIL import Image
except ImportError:
    print("You need to install pillow (6.x) for this project to work.")
    print("Do this in you command line: `pip install pillow`")
    input("Press enter to continue")
    quit()


def generate_char(dark, mode):
    """Select a courier character based on a darkness level."""
    if len(CHARS[dark]) > 0:
        # Select a random matching character
        if "l" in mode:
            char = CHARS[dark][0]
        else:
            char = CHARS[dark][random.randint(0, len(CHARS[dark]) - 1)]
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
                char = CHARS[dark][0]
            else:
                char = CHARS[dark][random.randint(0, len(CHARS[dark]) - 1)]
    return char


def ask(prompt, type_=None, min_=None, max_=None, range_=None):
    """Get user input of a certain type, with range and min/max options."""
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(
                        template.format(
                            " or ".join(
                                (
                                    ", ".join(map(str, range_[:-1])),
                                    str(range_[-1]),
                                )
                            )
                        )
                    )
        else:
            return ui


# i = 0
# for item in CHARS:
# if len(item) == 0:
# print(i)
# i += 1  # This prints all darknesses without a matching character.

# User inputs the path for the file:
user_input = input(
    'Enter the path of your file\n\
(absolute or relative path, type "demo" for a demo)\n'
)

question = """
Pick an option from the list below, or combine options.
r - regular (pick from full character set)
l - limited (pick only one character for each level of brightness)
n - non-text (don't pick letters or numbers)
"""
art_type = ask(question, str.lower, range_=("r", "l", "n", "ln", "nl"))
question = """
Now pick a size:
1 - largest size
3 - same size as original (approx)
5 - smallest size
"""
img_size = ask(question, int, 1, 5)

# Find the scalar variable used to convert from rgb to courier
LETTER_SCALE = constants.MAX_VAL - constants.MIN_VAL + 1
GRAY_SCALE = 255 - 1 + 1
SCALE = GRAY_SCALE / LETTER_SCALE

# Extract the data from constants into a useable form
CHARS = []
for i in range(constants.MAX_VAL + 1):
    CHARS.append([])
if "n" not in art_type:
    for letter, thickness in constants.CHAR_DARKNESS_TEXT_ONLY.items():
        CHARS[thickness].append(letter)
for letter, thickness in constants.CHAR_DARKNESS_NON_TEXT.items():
    CHARS[thickness].append(letter)


# Demo using included images:
if user_input == "demo":
    # Adjust path based on OS
    my_os = platform.system()
    if my_os == "Windows":
        img = Image.open("images\python.jpg")
    else:
        img = Image.open("images/python.jpg")
    # Print out some semi-useful info
    print(img.format, img.size)
    # Generate a 2-d list to hold output
    output_list = [
        [" "] * (img.size[0] // (3 * img_size)) for _ in range((img.size[1] // (5 * img_size)))
    ]
    # Loop through the image by pixels
    for row in range(img.size[1] // (5 * img_size)):
        for col in range(img.size[0] // (3 * img_size)):
            # grab the color of the current pixel
            color = img.getpixel((col * (3 * img_size), row * (5 * img_size)))
            gray = statistics.mean((color[0], color[1], color[2]))
            if img.format == "JPEG":
                darkness = round((255 - gray) / SCALE) + 1
                character = generate_char(darkness, art_type)
                output_list[row][col] = character
            else:
                if color[3] > 0:  # If the pixel isn't transparent:
                    darkness = round((255 - color[0]) / SCALE) + 1
                    character = generate_char(darkness, art_type)
                    output_list[row][col] = character

    # Print the output
    print("\n".join(map("".join, output_list)))
    print("You must view this in courier for the image to work.")
    # And save it to a file
    file = open("output.txt", "w")

    file.write("\n".join(map("".join, output_list)))

    file.close()
    print("The output has been saved to output.txt")


elif (".png" in user_input) or (".jpg" in user_input):
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
                gray = statistics.mean((color[0], color[1], color[2]))
                if img.format == "JPEG":
                    darkness = round((255 - gray) / SCALE) + 1
                    character = generate_char(darkness, art_type)
                    output_list[row][col] = character
                else:
                    if color[3] > 0:  # If the pixel isn't transparent:
                        darkness = round((255 - color[0]) / SCALE) + 1
                        character = generate_char(darkness, art_type)
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
    print("File must be a png or jpeg.\n\n\n")

# Wait for user before exiting.
input("Press enter to exit.")
