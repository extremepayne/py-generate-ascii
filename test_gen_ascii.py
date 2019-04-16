import constants
import gen_ascii

CHARS = gen_ascii.get_char_set(constants.CHAR_DARKNESS_TEXT_ONLY, constants.MAX_VAL)
more = gen_ascii.get_char_set(constants.CHAR_DARKNESS_NON_TEXT, constants.MAX_VAL)
i = 0
for smaller_list in CHARS:
    for character in more[i]:
        if character not in smaller_list:
            CHARS[i].append(character)
    i += 1
print(CHARS)
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
