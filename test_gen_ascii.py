import constants
import gen_ascii


def test_generate_char():
    """Tests gen_ascii.generate_char."""
    chars = gen_ascii.get_char_set(constants.CHAR_DARKNESS, constants.MAX_VAL)
    assert gen_ascii.generate_char(0, "r", chars) == " "
    assert gen_ascii.generate_char(3, "r", chars) == "`"
