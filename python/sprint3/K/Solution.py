def merge(arr: list, left: int, mid: int, right: int):
    result = [0] * (right-left)
    l, r, k = left, mid, 0
    while l < mid and r < right:
        if arr[l] <= arr[r]:
            result[k] = arr[l]
            l += 1
        else:
            result[k] = arr[r]
            r += 1
        k += 1
    while l < mid:
        result[k] = arr[l]
        l += 1
        k += 1
    while r < right:
        result[k] = arr[r]
        r += 1
        k += 1
    arr[left:right] = result
    return arr


def merge_sort(arr: list, left: int, right: int):
    if len(arr[left:right]) <= 1:  # базовый случай рекурсии
        return
    merge_sort(arr, left, left + (right-left)//2)
    merge_sort(arr, left + (right-left)//2, right)
    arr = merge(arr, left, left + (right-left)//2, right)



def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()