import unittest
from Geometry import calculate_rhombus_area



class TestCalculate_rhombus_area(unittest.TestCase):
    def test_calculate_rhombus_area_valid_input():
        result = Geometry.calculate_rhombus_area(10, 8)
        assert result == 40, f"Expected 40, got {result}"
    def test_calculate_rhombus_area_zero_diagonals():
        result = Geometry.calculate_rhombus_area(0, 8)
        assert result == 0, f"Expected 0, got {result}"
    def test_calculate_rhombus_area_negative_diagonal_1():
        try:
            Geometry.calculate_rhombus_area(-10, 8)
            assert False, "Expected ValueError for negative diagonal_1"
        except ValueError:
            pass
    def test_calculate_rhombus_area_negative_diagonal_2():
        try:
            Geometry.calculate_rhombus_area(10, -8)
            assert False, "Expected ValueError for negative diagonal_2"
        except ValueError:
            pass
    def test_calculate_rhombus_area_non_numeric_diagonal_1():
        try:
            Geometry.calculate_rhombus_area("ten", 8)
            assert False, "Expected TypeError for non-numeric diagonal_1"
        except TypeError:
            pass
    def test_calculate_rhombus_area_non_numeric_diagonal_2():
        try:
            Geometry.calculate_rhombus_area(10, "eight")
            assert False, "Expected TypeError for non-numeric diagonal_2"
        except TypeError:
            pass
    def test_calculate_rhombus_area_both_diagonals_zero():
        result = Geometry.calculate_rhombus_area(0, 0)
        assert result == 0, f"Expected 0, got {result}"
    def test_calculate_rhombus_area_large_values():
        result = Geometry.calculate_rhombus_area(1e6, 1e6)
        assert result == 5e11, f"Expected 5e11, got {result}"
    def test_calculate_rhombus_area_float_inputs():
        result = Geometry.calculate_rhombus_area(10.5, 8.2)
        assert result == 43.05, f"Expected 43.05, got {result}"

if __name__ == '__main__':
    unittest.main()
