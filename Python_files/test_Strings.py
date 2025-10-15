import unittest
from Strings import reverse_string



class TestReverse_string(unittest.TestCase):
    def test_reverse_string_valid_input():
        result = Strings.reverse_string("hello")
        assert result == "olleh"
    def test_reverse_string_empty_string():
        result = Strings.reverse_string("")
        assert result == ""
    def test_reverse_string_single_character():
        result = Strings.reverse_string("a")
        assert result == "a"
    def test_reverse_string_palindrome():
        result = Strings.reverse_string("madam")
        assert result == "madam"
    def test_reverse_string_with_spaces():
        result = Strings.reverse_string("hello world")
        assert result == "dlrow olleh"
    def test_reverse_string_with_numbers_and_symbols():
        result = Strings.reverse_string("123!@#")
        assert result == "#@!321"
    def test_reverse_string_with_unicode_characters():
        result = Strings.reverse_string("こんにちは")
        assert result == "はちにんこ"
    def test_reverse_string_none_input():
        try:
            Strings.reverse_string(None)
            assert False, "Expected a TypeError for None input"
        except TypeError:
            pass
    def test_reverse_string_invalid_type_input_list():
        try:
            Strings.reverse_string(["h", "e", "l", "l", "o"])
            assert False, "Expected a TypeError for list input"
        except TypeError:
            pass
    def test_reverse_string_invalid_type_input_integer():
        try:
            Strings.reverse_string(12345)
            assert False, "Expected a TypeError for integer input"
        except TypeError:
            pass

if __name__ == '__main__':
    unittest.main()
