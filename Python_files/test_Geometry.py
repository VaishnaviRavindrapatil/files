import unittest
from Geometry import calculate_circle_area



class TestCalculate_circle_area(unittest.TestCase):
    def test_calculate_circle_area_with_valid_radius():
        result = Geometry.calculate_circle_area(5)
        assert result == 78.53981633974483  # π * radius^2 for radius = 5
    def test_calculate_circle_area_with_zero_radius():
        result = Geometry.calculate_circle_area(0)
        assert result == 0  # Area should be 0 when radius is 0
    def test_calculate_circle_area_with_negative_radius():
        try:
            Geometry.calculate_circle_area(-3)
            assert False, "Expected ValueError for negative radius"
        except ValueError as e:
            assert str(e) == "Radius cannot be negative"
    def test_calculate_circle_area_with_non_numeric_radius():
        try:
            Geometry.calculate_circle_area("abc")
            assert False, "Expected TypeError for non-numeric radius"
        except TypeError as e:
            assert str(e) == "Radius must be a number"
    def test_calculate_circle_area_with_large_radius():
        result = Geometry.calculate_circle_area(1e6)
        assert result == 3.141592653589793 * (1e6)**2  # π * radius^2 for large radius
    def test_calculate_circle_area_with_float_radius():
        result = Geometry.calculate_circle_area(2.5)
        assert result == 19.634954084936208  # π * radius^2 for radius = 2.5

if __name__ == '__main__':
    unittest.main()
