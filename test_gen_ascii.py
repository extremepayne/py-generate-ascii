import constants
import gen_ascii


CHARS = gen_ascii.get_char_set(constants.CHAR_DARKNESS_TEXT_ONLY, constants.MAX_VAL)
CHARS.update(gen_ascii.get_char_set(constants.CHAR_DARKNESS_NON_TEXT, constants.MAX_VAL)

assert gen_ascii.generate_char(0, "r", CHARS) == " "
assert gen_ascii.generate_char(3, "r", CHARS) == "`"
assert gen_ascii.generate_char(21, "r", CHARS) in (
    "a",
    "n",
    "s",
    "y",
    "z",
    "*",
)
assert gen_ascii.generate_char(5, "l", CHARS) == "'"
