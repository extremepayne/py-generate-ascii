import platform
from PIL import Image
import constants
import gen_ascii

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

SCALE = gen_ascii.detirmine_scale(constants.MAX_VAL, constants.MIN_VAL)

assert gen_ascii.generate_char(0, "r", CHARS) == " "
assert gen_ascii.generate_char(21, "r", CHARS) in (
    "a",
    "n",
    "s",
    "y",
    "z",
    "*",
)
assert gen_ascii.generate_char(21, "l", CHARS) == "a"
assert gen_ascii.generate_char(3, "r", CHARS) in ("'", ".")
assert gen_ascii.generate_char(32, "l", CHARS) == "H"
assert gen_ascii.generate_char(34, "l", CHARS) == "@"


my_os = platform.system()
if my_os == "Windows":
    img = Image.open("images\python.jpg")
    img2 = Image.open("images\python.png")
else:
    img = Image.open("images/python.jpg")
    img2 = Image.open("images/python.png")

    gen_ascii.create_ascii(
        img, CHARS, "l", 4, SCALE
    )

    gen_ascii.create_ascii(
        img2, CHARS, "l", 3, SCALE
    )
