"""
Тесты для основного модуля main.py.
"""

import pytest
from main import solve_problem_1, solve_problem_2, solve_problem_3

class TestProblem1:
    """Тесты для решения проблемы 1: факториал."""

    def test_factorial_zero(self):
        """Тест факториала 0."""
        assert solve_problem_1(0) == 1

    def test_factorial_one(self):
        """Тест факториала 1."""
        assert solve_problem_1(1) == 1

    def test_factorial_five(self):
        """Тест факториала 5."""
        assert solve_problem_1(5) == 120

    def test_factorial_negative(self):
        """Тест отрицательного числа."""
        with pytest.raises(ValueError):
            solve_problem_1(-1)

class TestProblem2:
    """Тесты для решения проблемы 2: максимум в списке."""

    def test_max_single_element(self):
        """Тест списка с одним элементом."""
        assert solve_problem_2([5]) == 5

    def test_max_multiple_elements(self):
        """Тест списка с несколькими элементами."""
        assert solve_problem_2([1, 3, 2, 5, 4]) == 5

    def test_max_negative_numbers(self):
        """Тест списка с отрицательными числами."""
        assert solve_problem_2([-1, -3, -2]) == -1

    def test_max_empty_list(self):
        """Тест пустого списка."""
        with pytest.raises(ValueError):
            solve_problem_2([])

class TestProblem3:
    """Тесты для решения проблемы 3: сортировка пузырьком."""

    def test_sort_empty_list(self):
        """Тест сортировки пустого списка."""
        assert solve_problem_3([]) == []

    def test_sort_single_element(self):
        """Тест сортировки списка с одним элементом."""
        assert solve_problem_3([1]) == [1]

    def test_sort_already_sorted(self):
        """Тест сортировки уже отсортированного списка."""
        assert solve_problem_3([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_sort_reverse_sorted(self):
        """Тест сортировки обратно отсортированного списка."""
        assert solve_problem_3([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_sort_random_order(self):
        """Тест сортировки списка в случайном порядке."""
        assert solve_problem_3([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
