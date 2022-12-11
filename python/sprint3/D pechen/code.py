from typing import List, Tuple


def cookiesSort(n: int, cild_array, m: int, cookies_array):
    cild_values = [0] * (max(cild_array))
    cookies_values = [0] * (max(cookies_array))
    for value in cild_array:
        cild_values[value-1] += 1
    for value in cookies_array:
        cookies_values[value-1] += 1
    min_ind = len(cild_values) if len(cild_values) < len(cookies_values) else len(cookies_values)
    result = 0
    for i in range(min_ind):
        if cild_values[i] > cookies_values[i]:
            cild_values[i] -= cookies_values[i]
            result += cookies_values[i]
            cookies_values[i] = 0
        else:
            cookies_values[i] -= cild_values[i]
            for j in range(i, 0, -1):
                if cild_values[j] > cookies_values[i]:
            result += cild_values[i]
            cild_values[i]= 0
    print(result)


def read_input() -> Tuple[int, List[int], int, List[int]]:
    n = int(input())
    cild_list = list(map(int, input().strip().split()))
    m = int(input())
    cookies_list = list(map(int, input().strip().split()))
    return n, cild_list, m, cookies_list


if __name__ == '__main__':
    n, cild_list, m, cookies_list = read_input()
    cookiesSort(n, cild_list, m, cookies_list)
