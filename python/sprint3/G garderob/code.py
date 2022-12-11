from typing import List, Tuple


def wardrobeSort(n: int, array):
    counted_values = [0] * (max(array)+1)
    for value in array:
        counted_values[value] += 1
    index = 0
    for value in range(max(array)+1):
        for _ in range(0, counted_values[value]):
            array[index] = value
            index += 1
    return array


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return n, number_list


if __name__ == '__main__':
    n, number_list = read_input()
    if n > 0:
        result = wardrobeSort(n, number_list)
        print(' '.join(map(str,  result)))
