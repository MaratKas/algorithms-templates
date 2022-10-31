# https://contest.yandex.ru/contest/26365/problems/B/
from typing import List, Tuple

def zipper(a: List[int], b: List[int],n: int) -> List[int]:
    result = []
    for i in range(0, n):
        result.append(a[i])
        result.append(b[i])
    return result

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b, n

a, b, n = read_input()
print(" ".join(map(str, zipper(a, b, n))))
