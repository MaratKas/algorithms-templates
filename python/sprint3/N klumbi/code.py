from typing import List, Tuple


def clumb_sort(n, number_list, array):

    for j in range(0, len(number_list)):
        if number_list[j][0] > number_list[0][1]:
            break
        if number_list[j][1] > number_list[0][1]:
            number_list[0][1] = number_list[j][1]
    if len(number_list) <= 1:
        if array[-1][1] < number_list[0][1]:
            array.append(number_list[0])
        return array
    array.append(number_list[0])
    return clumb_sort(n, number_list[j:], array)


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    number_list = []
    for _ in range(n):
        number_list.append(list(map(int, input().split())))
    return n, number_list


if __name__ == '__main__':
    n, number_list = read_input()
    number_list.sort()
    array = []
    array = clumb_sort(n, number_list, array)
    for value in array:
        print(" ".join(map(str,  value)))
