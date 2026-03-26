"""Утилиты для определения типа треугольника."""

from __future__ import annotations


class IncorrectTriangleSides(ValueError):
    """Вызывается, если стороны не образуют корректный треугольник."""


def _validate_triangle_sides(a: float, b: float, c: float) -> None:
    sides = (a, b, c)

    if any(isinstance(side, bool) for side in sides):
        raise IncorrectTriangleSides("Стороны треугольника должны быть числами.")

    if not all(isinstance(side, (int, float)) for side in sides):
        raise IncorrectTriangleSides("Стороны треугольника должны быть числами.")

    if any(side <= 0 for side in sides):
        raise IncorrectTriangleSides("Стороны треугольника должны быть положительными.")

    x, y, z = sorted(float(side) for side in sides)
    if x + y <= z:
        raise IncorrectTriangleSides("Нарушено неравенство треугольника.")


def get_triangle_type(a: float, b: float, c: float) -> str:
    """Возвращает тип треугольника по длинам его сторон.

    Функция возвращает одно из следующих значений:
    - ``"nonequilateral"`` для корректного треугольника с тремя разными сторонами;
    - ``"isosceles"`` для корректного треугольника с двумя равными сторонами;
    - ``"equilateral"`` для корректного треугольника с тремя равными сторонами.

    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(5, 5, 8)
    'isosceles'
    >>> get_triangle_type(7, 7, 7)
    'equilateral'
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
    ...
    triangle_func.IncorrectTriangleSides: Нарушено неравенство треугольника.
    >>> get_triangle_type(0, 4, 4)
    Traceback (most recent call last):
    ...
    triangle_func.IncorrectTriangleSides: Стороны треугольника должны быть положительными.
    """

    _validate_triangle_sides(a, b, c)

    if a == b == c:
        return "equilateral"

    if a == b or b == c or a == c:
        return "isosceles"

    return "nonequilateral"
