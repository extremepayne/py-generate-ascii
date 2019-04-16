import constants
import gen_ascii

CHARS = gen_ascii.get_char_set(constants.CHAR_DARKNESS, constants.MAX_VAL)
if gen_ascii.generate_char(0, "r", CHARS) != " ":
    raise AssertionError
if gen_ascii.generate_char(3, "r", CHARS) != "`":
    raise AssertionError
