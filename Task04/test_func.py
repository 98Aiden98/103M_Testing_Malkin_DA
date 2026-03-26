"""Тесты unittest для get_triangle_type."""

from __future__ import annotations

import unittest

from Task04.triangle_func import IncorrectTriangleSides, get_triangle_type


class GetTriangleTypeTests(unittest.TestCase):
    def test_returns_nonequilateral_for_scalene_triangle(self) -> None:
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    def test_returns_isosceles_for_valid_isosceles_triangle(self) -> None:
        self.assertEqual(get_triangle_type(5, 5, 8), "isosceles")

    def test_returns_equilateral_for_equal_sides(self) -> None:
        self.assertEqual(get_triangle_type(7, 7, 7), "equilateral")

    def test_raises_for_zero_side(self) -> None:
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 4)

    def test_raises_for_triangle_inequality_violation(self) -> None:
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    def test_raises_for_non_numeric_side(self) -> None:
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("3", 4, 5)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
