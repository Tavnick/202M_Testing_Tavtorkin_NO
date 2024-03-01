import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleFunctions(unittest.TestCase):
    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(5, 5, 4), "isosceles")
    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")

    def test_incorrect_triangle_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-2, 3, 2)

        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 5)

        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 4, 10)

if __name__ == '__main__':
    unittest.main()