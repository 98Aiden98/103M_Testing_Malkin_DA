"""Тесты pytest для Triangle."""

from __future__ import annotations

import pytest

from Task04.triangle_class import IncorrectTriangleSides, Triangle


def test_triangle_object_is_created_for_valid_sides() -> None:
    triangle = Triangle(3, 4, 5)

    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5


def test_triangle_type_returns_equilateral() -> None:
    assert Triangle(6, 6, 6).triangle_type() == "equilateral"


def test_triangle_type_returns_isosceles() -> None:
    assert Triangle(5, 5, 8).triangle_type() == "isosceles"


def test_triangle_type_returns_nonequilateral() -> None:
    assert Triangle(4, 5, 6).triangle_type() == "nonequilateral"


def test_perimeter_returns_sum_of_sides() -> None:
    assert Triangle(2.5, 3.5, 4.0).perimeter() == pytest.approx(10.0)


@pytest.mark.parametrize(
    ("a", "b", "c"),
    [
        (0, 4, 4),
        (-1, 4, 4),
        (1, 2, 3),
        (True, 4, 5),
    ],
)
def test_invalid_triangle_creation_raises(a: float, b: float, c: float) -> None:
    with pytest.raises(IncorrectTriangleSides):
        Triangle(a, b, c)
