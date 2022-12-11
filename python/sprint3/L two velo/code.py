from typing import List, Tuple


def binarySearch(arr, x, left, right):
    if right <= left and arr[right] < x:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x and (mid == 0 or arr[mid-1] < x): # центральный элемент — искомый
        return mid + 1
    elif x <= arr[mid]: # искомый элемент меньше центрального
                       # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else: # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)


def buy_bike(n: str, number_list: str, price: int):
    rez = binarySearch(number_list, price, 0, n)
    if rez != -1:
        rez2 = binarySearch(number_list, price * 2, rez, n)
    else:
        rez2 = -1
    return str(rez) + " " + str(rez2)


def read_input() -> Tuple[int, List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    price = int(input())
    return n, number_list, price


if __name__ == '__main__':
    n, number_list, price = read_input()
    result = buy_bike(n-1, number_list, price)
    print(result)
