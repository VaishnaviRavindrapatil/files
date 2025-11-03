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


class TestTo_lowercase(unittest.TestCase):
    def test_to_lowercase_valid_string():
        result = Strings.to_lowercase("HELLO")
        assert result == "hello"
    def test_to_lowercase_mixed_case_string():
        result = Strings.to_lowercase("HeLLo WoRLd")
        assert result == "hello world"
    def test_to_lowercase_empty_string():
        result = Strings.to_lowercase("")
        assert result == ""
    def test_to_lowercase_already_lowercase_string():
        result = Strings.to_lowercase("already lowercase")
        assert result == "already lowercase"
    def test_to_lowercase_numeric_string():
        result = Strings.to_lowercase("1234")
        assert result == "1234"
    def test_to_lowercase_special_characters():
        result = Strings.to_lowercase("!@#$%^&*()")
        assert result == "!@#$%^&*()"
    def test_to_lowercase_mixed_alphanumeric_special():
        result = Strings.to_lowercase("HeLLo123!@#")
        assert result == "hello123!@#"
    def test_to_lowercase_none_input():
        try:
            Strings.to_lowercase(None)
            assert False, "Expected an exception for None input"
        except TypeError:
            pass
    def test_to_lowercase_integer_input():
        try:
            Strings.to_lowercase(12345)
            assert False, "Expected an exception for integer input"
        except TypeError:
            pass
    def test_to_lowercase_list_input():
        try:
            Strings.to_lowercase(["HELLO", "WORLD"])
            assert False, "Expected an exception for list input"
        except TypeError:
            pass

if __name__ == '__main__':
    unittest.main()


class TestRemove_duplicates(unittest.TestCase):
    def test_remove_duplicates_valid_input():
        result = Strings.remove_duplicates("aabbcc")
        assert result == "abc", f"Expected 'abc', got {result}"
    def test_remove_duplicates_empty_string():
        result = Strings.remove_duplicates("")
        assert result == "", f"Expected '', got {result}"
    def test_remove_duplicates_single_character():
        result = Strings.remove_duplicates("a")
        assert result == "a", f"Expected 'a', got {result}"
    def test_remove_duplicates_no_duplicates():
        result = Strings.remove_duplicates("abc")
        assert result == "abc", f"Expected 'abc', got {result}"
    def test_remove_duplicates_special_characters():
        result = Strings.remove_duplicates("!!@@##")
        assert result == "!@#", f"Expected '!@#', got {result}"
    def test_remove_duplicates_numbers_in_string():
        result = Strings.remove_duplicates("112233")
        assert result == "123", f"Expected '123', got {result}"
    def test_remove_duplicates_mixed_characters():
        result = Strings.remove_duplicates("a1a2b3b4")
        assert result == "a1b234", f"Expected 'a1b234', got {result}"
    def test_remove_duplicates_non_string_input():
        try:
            Strings.remove_duplicates(12345)
            assert False, "Expected TypeError, but no exception was raised"
        except TypeError:
            pass  # Expected behavior
    def test_remove_duplicates_none_input():
        try:
            Strings.remove_duplicates(None)
            assert False, "Expected TypeError, but no exception was raised"
        except TypeError:
            pass  # Expected behavior
    def test_remove_duplicates_whitespace_string():
        result = Strings.remove_duplicates("  ")
        assert result == " ", f"Expected ' ', got {result}"
    def test_remove_duplicates_mixed_whitespace_and_characters():
        result = Strings.remove_duplicates("a a b b")
        assert result == "a b", f"Expected 'a b', got {result}"

if __name__ == '__main__':
    unittest.main()


class TestRemove_extra_spaces(unittest.TestCase):
    def test_remove_extra_spaces_valid_single_space():
        input_text = "This  is   a    test"
        expected_output = "This is a test"
        self.assertEqual(Strings.remove_extra_spaces(input_text), expected_output)
    def test_remove_extra_spaces_valid_leading_trailing_spaces():
        input_text = "   Leading and trailing spaces   "
        expected_output = "Leading and trailing spaces"
        self.assertEqual(Strings.remove_extra_spaces(input_text), expected_output)
    def test_remove_extra_spaces_valid_only_spaces():
        input_text = "         "
        expected_output = ""
        self.assertEqual(Strings.remove_extra_spaces(input_text), expected_output)
    def test_remove_extra_spaces_valid_no_extra_spaces():
        input_text = "NoExtraSpacesHere"
        expected_output = "NoExtraSpacesHere"
        self.assertEqual(Strings.remove_extra_spaces(input_text), expected_output)
    def test_remove_extra_spaces_valid_empty_string():
        input_text = ""
        expected_output = ""
        self.assertEqual(Strings.remove_extra_spaces(input_text), expected_output)
    def test_remove_extra_spaces_valid_newline_and_tabs():
        input_text = "   This\nis\ta test    "
        expected_output = "This is a test"
        self.assertEqual(Strings.remove_extra_spaces(input_text), expected_output)
    def test_remove_extra_spaces_invalid_non_string_input():
        input_text = 12345  # Non-string input
        with self.assertRaises(TypeError):
            Strings.remove_extra_spaces(input_text)
    def test_remove_extra_spaces_invalid_none_input():
        input_text = None  # None input
        with self.assertRaises(TypeError):
            Strings.remove_extra_spaces(input_text)

if __name__ == '__main__':
    unittest.main()


class TestReverse_and_lowercase(unittest.TestCase):
    def test_reverse_and_lowercase_valid_string():
        result = Strings.reverse_and_lowercase("HelloWorld")
        assert result == "dlrowolleh"
    def test_reverse_and_lowercase_empty_string():
        result = Strings.reverse_and_lowercase("")
        assert result == ""
    def test_reverse_and_lowercase_string_with_numbers():
        result = Strings.reverse_and_lowercase("Python123")
        assert result == "321nohtyp"
    def test_reverse_and_lowercase_all_lowercase_string():
        result = Strings.reverse_and_lowercase("lowercase")
        assert result == "esacrewol"
    def test_reverse_and_lowercase_all_uppercase_string():
        result = Strings.reverse_and_lowercase("UPPERCASE")
        assert result == "esacreppu"
    def test_reverse_and_lowercase_mixed_case_string():
        result = Strings.reverse_and_lowercase("MiXeDCasE")
        assert result == "esacdexim"
    def test_reverse_and_lowercase_special_characters():
        result = Strings.reverse_and_lowercase("!@#Test123$")
        assert result == "$321tset#@!"
    def test_reverse_and_lowercase_whitespace_string():
        result = Strings.reverse_and_lowercase("  Space  ")
        assert result == "  ecaps  "
    def test_reverse_and_lowercase_invalid_input_integer():
        try:
            Strings.reverse_and_lowercase(12345)
            assert False, "Expected TypeError for integer input"
        except TypeError:
            pass
    def test_reverse_and_lowercase_invalid_input_none():
        try:
            Strings.reverse_and_lowercase(None)
            assert False, "Expected TypeError for None input"
        except TypeError:
            pass
    def test_reverse_and_lowercase_invalid_input_list():
        try:
            Strings.reverse_and_lowercase(["a", "b", "c"])
            assert False, "Expected TypeError for list input"
        except TypeError:
            pass

if __name__ == '__main__':
    unittest.main()


class TestReverse_and_modify_string(unittest.TestCase):
    def test_reverse_and_modify_string_valid_input():
        # Test valid input with a normal string
        result = Strings.reverse_and_modify_string("hello")
        expected = "olleh"
        assert result == expected, f"Expected {expected}, but got {result}"
    def test_reverse_and_modify_string_empty_string():
        # Test valid input with an empty string
        result = Strings.reverse_and_modify_string("")
        expected = ""
        assert result == expected, f"Expected {expected}, but got {result}"
    def test_reverse_and_modify_string_single_character():
        # Test valid input with a single character
        result = Strings.reverse_and_modify_string("a")
        expected = "a"
        assert result == expected, f"Expected {expected}, but got {result}"
    def test_reverse_and_modify_string_whitespace_string():
        # Test valid input with a string containing only whitespace
        result = Strings.reverse_and_modify_string("   ")
        expected = "   "
        assert result == expected, f"Expected {expected}, but got {result}"
    def test_reverse_and_modify_string_special_characters():
        # Test valid input with special characters
        result = Strings.reverse_and_modify_string("!@#123")
        expected = "321#@!"
        assert result == expected, f"Expected {expected}, but got {result}"
    def test_reverse_and_modify_string_numeric_string():
        # Test valid input with a numeric string
        result = Strings.reverse_and_modify_string("12345")
        expected = "54321"
        assert result == expected, f"Expected {expected}, but got {result}"
    def test_reverse_and_modify_string_mixed_characters():
        # Test valid input with a mix of characters
        result = Strings.reverse_and_modify_string("a1b2c3")
        expected = "3c2b1a"
        assert result == expected, f"Expected {expected}, but got {result}"
    def test_reverse_and_modify_string_none_input():
        # Test invalid input with None
        try:
            Strings.reverse_and_modify_string(None)
            assert False, "Expected TypeError, but no exception was raised"
        except TypeError:
            pass
    def test_reverse_and_modify_string_integer_input():
        # Test invalid input with an integer
        try:
            Strings.reverse_and_modify_string(12345)
            assert False, "Expected TypeError, but no exception was raised"
        except TypeError:
            pass
    def test_reverse_and_modify_string_list_input():
        # Test invalid input with a list
        try:
            Strings.reverse_and_modify_string(["a", "b", "c"])
            assert False, "Expected TypeError, but no exception was raised"
        except TypeError:
            pass
    def test_reverse_and_modify_string_boolean_input():
        # Test invalid input with a boolean
        try:
            Strings.reverse_and_modify_string(True)
            assert False, "Expected TypeError, but no exception was raised"
        except TypeError:
            pass
    def test_reverse_and_modify_string_object_input():
        # Test invalid input with an object
        try:
            Strings.reverse_and_modify_string(object())
            assert False, "Expected TypeError, but no exception was raised"
        except TypeError:
            pass

if __name__ == '__main__':
    unittest.main()
