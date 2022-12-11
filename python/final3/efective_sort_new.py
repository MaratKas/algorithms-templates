# 78690222
from typing import List, Any
from random import randint


def effective_quick_sort(rating: list) -> list:
    """Эффективная сортировка"""

    def _quick_sort(rating: list, start: int, end: int) -> None:
        if start >= end:
            return -1
        mid_rnd = rating[randint(start, end)]
        left, right = start, end
        while left <= right:
            while rating[left] < mid_rnd:
                left += 1
            while rating[right] > mid_rnd:
                right -= 1
            if left <= right:
                rating[left], rating[right] = rating[right], rating[left]
                left += 1
                right -= 1
        _quick_sort(rating, start, right)
        _quick_sort(rating, left, end)
    start = 0
    end = len(rating) - 1
    _quick_sort(rating, start, end)
    return rating


class Rating_user:
    """Клас."""
    def __init__(self, date: List[Any]):
        self.solutions: int = -int(date[1])
        self.staff: int = int(date[2])
        self.login: str = date[0]

    def __gt__(self, other):
        if self.solutions == other.solutions:
            return self.login > other.login if self.staff == other.staff else self.staff > other.staff
        return self.solutions > other.solutions

    def __str__(self):
        return self.login


def read_input() -> list:
    """Ввод тестовых данных."""
    count_member = int(input())
    users = [Rating_user(input().split()) for _ in range(count_member)]
    return users


if __name__ == '__main__':
    users = read_input()
    effective_quick_sort(users)
    print(*users, sep='\n')
