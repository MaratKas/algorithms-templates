from typing import List, Tuple


def bubbleSort(n: str, number_list: str):
    for j in range(1, n):
        key = True
        for i in range(0, n  - j):
            if number_list[i] > number_list[i+1]:
                number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
                key = False
        if key and j != 1:
            break
        else:
            print(" ".join(map(str, number_list)))

def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return n, number_list


if __name__ == '__main__':
    n, number_list = read_input()
    bubbleSort(n, number_list)
