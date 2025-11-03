import unittest
from Geometry import area_of_rhombus



class TestArea_of_rhombus(unittest.TestCase):
    def test_area_of_rhombus_valid_inputs(self):
        result = Geometry.area_of_rhombus(10, 5)
        self.assertEqual(result, 25)
    def test_area_of_rhombus_valid_floats(self):
        result = Geometry.area_of_rhombus(7.5, 4.2)
        self.assertAlmostEqual(result, 15.75)
    def test_area_of_rhombus_zero_diagonals(self):
        result = Geometry.area_of_rhombus(0, 10)
        self.assertEqual(result, 0)
    def test_area_of_rhombus_negative_diagonal1(self):
        with self.assertRaises(ValueError):
            Geometry.area_of_rhombus(-8, 6)
    def test_area_of_rhombus_negative_diagonal2(self):
        with self.assertRaises(ValueError):
            Geometry.area_of_rhombus(8, -6)
    def test_area_of_rhombus_non_numeric_diagonal1(self):
        with self.assertRaises(TypeError):
            Geometry.area_of_rhombus("10", 5)
    def test_area_of_rhombus_non_numeric_diagonal2(self):
        with self.assertRaises(TypeError):
            Geometry.area_of_rhombus(10, "5")
    def test_area_of_rhombus_both_diagonals_non_numeric(self):
        with self.assertRaises(TypeError):
            Geometry.area_of_rhombus("10", "5")
    def test_area_of_rhombus_none_as_input(self):
        with self.assertRaises(TypeError):
            Geometry.area_of_rhombus(None, 5)
    def test_area_of_rhombus_one_diagonal_as_none(self):
        with self.assertRaises(TypeError):
            Geometry.area_of_rhombus(10, None)
    def test_area_of_rhombus_large_numbers(self):
        result = Geometry.area_of_rhombus(1e6, 2e6)
        self.assertEqual(result, 1e12)
    def test_area_of_rhombus_small_numbers(self):
        result = Geometry.area_of_rhombus(1e-6, 2e-6)
        self.assertAlmostEqual(result, 1e-12)

if __name__ == '__main__':
    unittest.main()
