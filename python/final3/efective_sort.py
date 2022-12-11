# 77450107
from typing import Tuple
from random import randint


def effective_quick_sort(rating: list, left: int, right: int) -> list:
    """Эффективная сортировка"""
    if left >= right:
        return -1
    mid_rnd = rating[randint(left, right)]
    l_counter = left
    r_counter = right
    while l_counter <= r_counter:
        while rating[l_counter] < mid_rnd:
            l_counter += 1
        while rating[r_counter] > mid_rnd:
            r_counter -= 1
        if l_counter <= r_counter:
            rating[l_counter], rating[r_counter] = rating[r_counter], rating[l_counter]
            l_counter += 1
            r_counter -= 1
    effective_quick_sort(rating, left, r_counter)
    effective_quick_sort(rating, l_counter, right)
    return rating


def reformat(login: str, solutions: int, staff: int) -> tuple:
    """Форматирование данных."""
    return (-int(solutions), int(staff), login)


def read_input() -> Tuple[int, list]:
    """Ввод тестовых данных."""
    member = int(input())
    rating = [reformat(*input().split()) for _ in range(member)]
    return member, rating


if __name__ == '__main__':
    member, rating = read_input()
    left = 0
    right = member - 1
    if member == 1:
        print(rating[0][2])
    else:
        result = effective_quick_sort(rating, left, right)
        for item in result:
            print(item[2])
