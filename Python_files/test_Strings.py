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


class TestTo_uppercase(unittest.TestCase):
    def test_to_uppercase_valid_string():
        result = Strings.to_uppercase("hello")
        assert result == "HELLO"
    def test_to_uppercase_empty_string():
        result = Strings.to_uppercase("")
        assert result == ""
    def test_to_uppercase_already_uppercase():
        result = Strings.to_uppercase("WORLD")
        assert result == "WORLD"
    def test_to_uppercase_mixed_case_string():
        result = Strings.to_uppercase("HeLLo WoRLd")
        assert result == "HELLO WORLD"
    def test_to_uppercase_with_numbers_and_symbols():
        result = Strings.to_uppercase("123!@#abcDEF")
        assert result == "123!@#ABCDEF"
    def test_to_uppercase_with_whitespace():
        result = Strings.to_uppercase("  test string  ")
        assert result == "  TEST STRING  "
    def test_to_uppercase_none_input():
        try:
            Strings.to_uppercase(None)
            assert False, "Expected a TypeError for None input"
        except TypeError:
            pass
    def test_to_uppercase_int_input():
        try:
            Strings.to_uppercase(123)
            assert False, "Expected a TypeError for integer input"
        except TypeError:
            pass
    def test_to_uppercase_list_input():
        try:
            Strings.to_uppercase(["a", "b", "c"])
            assert False, "Expected a TypeError for list input"
        except TypeError:
            pass
    def test_to_uppercase_bool_input():
        try:
            Strings.to_uppercase(True)
            assert False, "Expected a TypeError for boolean input"
        except TypeError:
            pass

if __name__ == '__main__':
    unittest.main()
