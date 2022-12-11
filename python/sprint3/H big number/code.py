from typing import List, Tuple


def is_first_num(num_1, num_2):  # функция-компаратор
    return int(num_1 + num_2) < int(num_2 + num_1)


def big_number(n: str, number_list: str, less):
    for j in range(1, n):
        key = True
        for i in range(0, n  - j):
            if less(number_list[i], number_list[i+1]):
                number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
                key = False
        if key:
            return("".join(map(str, number_list)))
    return("".join(map(str, number_list)))


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    number_list = list(input().strip().split())
    return n, number_list


if __name__ == '__main__':
    n, number_list = read_input()
    print(big_number(n, number_list, is_first_num))
