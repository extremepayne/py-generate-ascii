"""Generate ascii art from image."""
# pylint: disable=C0103

# Imports
import os
import platform
import constants  # Local; has some variable I didn't want cluttering this file
import gen_ascii

# PIL used to process images
try:
    from PIL import Image
except ImportError:
    print("You need to install pillow (6.x) for this project to work.")
    print("Do this in you command line: `pip install pillow`")
    input("Press enter to continue")
    quit()


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

# Extract the data from constants into a useable form
if "n" not in art_type:
    CHARS = gen_ascii.get_char_set(
        constants.CHAR_DARKNESS_TEXT_ONLY, constants.MAX_VAL
    )
    more = gen_ascii.get_char_set(
        constants.CHAR_DARKNESS_NON_TEXT, constants.MAX_VAL
    )
    i = 0
    for smaller_list in CHARS:
        for character in more[i]:
            if character not in smaller_list:
                CHARS[i].append(character)
        i += 1
else:
    CHARS = gen_ascii.get_char_set(
        constants.CHAR_DARKNESS_NON_TEXT, constants.MAX_VAL
    )

# i = 0
# for item in CHARS:
#    if len(item) == 0:
#        print(i)
#    i += 1  # This prints all darknesses without a matching character.

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
    output = gen_ascii.create_ascii(
        img, CHARS, art_type, img_size, constants.MAX_VAL, constants.MIN_VAL
    )

    # Print the output
    print("\n".join(map("".join, output)))
    print("You must view this in courier for the image to work.")
    # And save it to a file
    file = open("output.txt", "w")

    file.write("\n".join(map("".join, output)))

    file.close()
    print("The output has been saved to output.txt")


elif (".png" in user_input) or (".jpg" in user_input):
    if os.path.exists(user_input):
        img = Image.open(user_input)
        # Print out some semi-useful info
        print(img.format, img.size)
        output = gen_ascii.create_ascii(
            img,
            CHARS,
            art_type,
            img_size,
            constants.MAX_VAL,
            constants.MIN_VAL,
        )
        # Print the output
        print("\n".join(map("".join, output)))
        print("You must view this in courier for the image to work.")
        # And save it to a file
        file = open("output.txt", "w")

        file.write("\n".join(map("".join, output)))

        file.close()
        print("The output has been saved to output.txt")
    else:
        print("That path does not exist.")

else:
    print("File must be a png or jpeg.\n\n\n")

# Wait for user before exiting.
input("Press enter to exit.")
