"""Утилиты для решения квадратных уравнений."""

from __future__ import annotations

from math import sqrt


def solve_quadratic(a: float, b: float, c: float) -> tuple[float, ...]:
    """Возвращает действительные корни ax^2 + bx + c = 0 по возрастанию.

    Функция возвращает:
    - пустой кортеж, если действительных корней нет;
    - кортеж из одного элемента, если корень один;
    - кортеж из двух элементов, если корней два.

    Если ``a`` равно нулю, вызывается ValueError, потому что уравнение
    в этом случае не является квадратным.
    """

    if a == 0:
        raise ValueError("Коэффициент 'a' не должен быть равен нулю.")

    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return ()

    if discriminant == 0:
        return (-b / (2 * a),)

    root_delta = sqrt(discriminant)
    roots = (
        (-b - root_delta) / (2 * a),
        (-b + root_delta) / (2 * a),
    )
    return tuple(sorted(roots))
