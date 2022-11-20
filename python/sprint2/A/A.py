from typing import List, Tuple

def get_monitoring(matrix: List[List[int]], n: int, m: int,) -> List[List[int]]:
    res = [[0]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][i] = matrix[i][j]
    return res


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    return matrix, n, m


if __name__ == '__main__':
    matrix, n, m = read_input()
    for i in get_monitoring(matrix, n, m):
        print(*i)
