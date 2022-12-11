# 77903552

from typing import List, Tuple


def broken_search(nums: List[int], target: int) -> int:
    """Поиск в сломанном массиве."""
    left = 0
    right = len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        elif nums[mid] <= nums[left]:
            if nums[mid] < target <= nums[left]:
                left = mid + 1
            else:
                right = mid
    return result


def read_input() -> Tuple[int, int, List[int]]:
    """Ввод тестовых данных."""
    len_list = int(input())
    target = int(input())
    mass_list = [int(element) for element in input().strip().split()]
    return len_list, target, mass_list


if __name__ == '__main__':
    len_list, target, mass_list = read_input()
    print(broken_search(mass_list, target))
