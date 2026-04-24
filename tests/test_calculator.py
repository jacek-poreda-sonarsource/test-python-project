import pytest
from test_python_project.calculator import (
    add,
    subtract,
    multiply,
    divide,
    calculate,
    complex_calculation,
)


class TestAdd:
    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -1) == -2

    def test_add_zero(self):
        assert add(0, 0) == 0

    def test_add_float(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_subtract_positive(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative(self):
        assert subtract(-1, -1) == 0


class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(3, 4) == 12

    def test_multiply_zero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    def test_divide_positive(self):
        assert divide(10, 2) == 5.0

    def test_divide_by_zero(self):
        assert divide(10, 0) is None


class TestCalculate:
    def test_calculate_add(self):
        assert calculate("add", 2, 3) == 5

    def test_calculate_subtract(self):
        assert calculate("subtract", 5, 3) == 2

    def test_calculate_multiply(self):
        assert calculate("multiply", 3, 4) == 12

    def test_calculate_divide(self):
        assert calculate("divide", 10, 2) == pytest.approx(5.0)

    def test_calculate_divide_by_zero(self):
        assert calculate("divide", 10, 0) is None

    def test_calculate_power(self):
        assert calculate("power", 2, 3) == 8

    def test_calculate_unknown(self):
        assert calculate("modulo", 10, 3) is None

    def test_calculate_strict_add_valid(self):
        assert calculate("add", 2, 3, strict=True) == 5

    def test_calculate_strict_add_invalid_a(self):
        assert calculate("add", "two", 3, strict=True) is None

    def test_calculate_strict_add_invalid_b(self):
        assert calculate("add", 2, "three", strict=True) is None

    def test_calculate_strict_subtract_valid(self):
        assert calculate("subtract", 5, 3, strict=True) == 2

    def test_calculate_strict_subtract_invalid_a(self):
        assert calculate("subtract", "five", 3, strict=True) is None

    def test_calculate_strict_subtract_invalid_b(self):
        assert calculate("subtract", 5, "three", strict=True) is None


class TestComplexCalculation:
    def test_all_ones(self):
        assert complex_calculation(1, 1, 1, 1, 1, 1, 1, 1) == 8

    def test_sequential(self):
        assert complex_calculation(1, 2, 3, 4, 5, 6, 7, 8) == 36
