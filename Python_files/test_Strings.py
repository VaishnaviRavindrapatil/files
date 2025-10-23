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


class TestIs_palindrome(unittest.TestCase):
    def test_is_palindrome_with_palindrome_string():
        result = Strings.is_palindrome("radar")
        assert result is True
    def test_is_palindrome_with_non_palindrome_string():
        result = Strings.is_palindrome("hello")
        assert result is False
    def test_is_palindrome_with_empty_string():
        result = Strings.is_palindrome("")
        assert result is True
    def test_is_palindrome_with_single_character():
        result = Strings.is_palindrome("a")
        assert result is True
    def test_is_palindrome_with_mixed_case_palindrome():
        result = Strings.is_palindrome("RaceCar")
        assert result is True
    def test_is_palindrome_with_mixed_case_non_palindrome():
        result = Strings.is_palindrome("HelloWorld")
        assert result is False
    def test_is_palindrome_with_spaces_and_palindrome():
        result = Strings.is_palindrome("A man a plan a canal Panama")
        assert result is True
    def test_is_palindrome_with_spaces_and_non_palindrome():
        result = Strings.is_palindrome("This is not a palindrome")
        assert result is False
    def test_is_palindrome_with_numbers_and_palindrome():
        result = Strings.is_palindrome("12321")
        assert result is True
    def test_is_palindrome_with_numbers_and_non_palindrome():
        result = Strings.is_palindrome("12345")
        assert result is False
    def test_is_palindrome_with_special_characters_and_palindrome():
        result = Strings.is_palindrome("!@#$%^&^%$#@!")
        assert result is True
    def test_is_palindrome_with_special_characters_and_non_palindrome():
        result = Strings.is_palindrome("!@#$abc$#@!")
        assert result is False
    def test_is_palindrome_with_none_input():
        try:
            Strings.is_palindrome(None)
            assert False, "Expected exception for None input"
        except TypeError:
            pass
    def test_is_palindrome_with_numeric_input():
        try:
            Strings.is_palindrome(12321)
            assert False, "Expected exception for numeric input"
        except TypeError:
            pass
    def test_is_palindrome_with_list_input():
        try:
            Strings.is_palindrome(["a", "b", "b", "a"])
            assert False, "Expected exception for list input"
        except TypeError:
            pass

if __name__ == '__main__':
    unittest.main()
