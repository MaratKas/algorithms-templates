from typing import Tuple


def find_serch(str_1: str, str_2: str):
    if str_1 == "":
        return True
    start = str_2.find(str_1[0])
    if start == -1:
        return False
    return find_serch(str_1[1:], str_2[start:])


def read_input() -> Tuple[str, str]:
    str_1 = str(input())
    str_2 = str(input())
    return str_1, str_2


if __name__ == '__main__':
    str_1, str_2 = read_input()
    print(find_serch(str_1, str_2))
