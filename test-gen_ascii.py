import constants
import gen_ascii

assert gen_ascii.generate_char(0, "r", constants.CHAR_DARKNESS) == " "
assert gen_ascii.generate_char(3, "r", constants.CHAR_DARKNESS) == "`"
