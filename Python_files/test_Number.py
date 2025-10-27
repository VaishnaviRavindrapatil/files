import unittest
from Number import add_ten



class TestAdd_ten(unittest.TestCase):
    def test_add_ten_valid_input():
        result = Number.add_ten(5)
        assert result == 15, f"Expected 15 but got {result}"
    def test_add_ten_negative_input():
        result = Number.add_ten(-10)
        assert result == 0, f"Expected 0 but got {result}"
    def test_add_ten_zero_input():
        result = Number.add_ten(0)
        assert result == 10, f"Expected 10 but got {result}"
    def test_add_ten_large_input():
        result = Number.add_ten(1000)
        assert result == 1010, f"Expected 1010 but got {result}"
    def test_add_ten_invalid_input_string():
        try:
            Number.add_ten("5")
        except TypeError:
            pass
        else:
            assert False, "Expected TypeError for string input"
    def test_add_ten_invalid_input_none():
        try:
            Number.add_ten(None)
        except TypeError:
            pass
        else:
            assert False, "Expected TypeError for None input"
    def test_add_ten_invalid_input_list():
        try:
            Number.add_ten([10])
        except TypeError:
            pass
        else:
            assert False, "Expected TypeError for list input"
    def test_add_ten_float_input():
        result = Number.add_ten(5.5)
        assert result == 15.5, f"Expected 15.5 but got {result}"
    def test_add_ten_boolean_input():
        result = Number.add_ten(True)
        assert result == 11, f"Expected 11 but got {result}"
    def test_add_ten_invalid_input_dict():
        try:
            Number.add_ten({"key": 10})
        except TypeError:
            pass
        else:
            assert False, "Expected TypeError for dict input"

if __name__ == '__main__':
    unittest.main()


class TestFactorial(unittest.TestCase):
    def test_factorial_positive_integer():
        result = Number.factorial(5)
        assert result == 120
    def test_factorial_zero():
        result = Number.factorial(0)
        assert result == 1
    def test_factorial_one():
        result = Number.factorial(1)
        assert result == 1
    def test_factorial_large_number():
        result = Number.factorial(10)
        assert result == 3628800
    def test_factorial_negative_number():
        with pytest.raises(ValueError):
            Number.factorial(-5)
    def test_factorial_non_integer():
        with pytest.raises(TypeError):
            Number.factorial(3.5)
    def test_factorial_string_input():
        with pytest.raises(TypeError):
            Number.factorial("5")
    def test_factorial_none_input():
        with pytest.raises(TypeError):
            Number.factorial(None)
    def test_factorial_boolean_input():
        result = Number.factorial(True)
        assert result == 1

if __name__ == '__main__':
    unittest.main()
