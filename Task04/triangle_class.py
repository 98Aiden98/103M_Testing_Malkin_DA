"""Реализация класса Triangle."""

from __future__ import annotations

from Task04.triangle_func import IncorrectTriangleSides, get_triangle_type


class Triangle:
    """Представляет корректный треугольник."""

    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

        get_triangle_type(a, b, c)

    def triangle_type(self) -> str:
        """Возвращает тип треугольника."""

        return get_triangle_type(self.a, self.b, self.c)

    def perimeter(self) -> float:
        """Возвращает периметр треугольника."""

        return self.a + self.b + self.c


__all__ = ["Triangle", "IncorrectTriangleSides"]
