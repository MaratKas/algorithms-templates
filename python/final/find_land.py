from typing import List
# ID 73763969.

Street = List[int]


def get_best_zero(street: Street, n: int) -> Street:
    """Постройка карты с растоянием до пустых участков."""
    street_zero = [0] * n
    zero_old_ind = None
    for index, element in enumerate(street, 0):
        if element == 0:
            if zero_old_ind is None:
                street_zero[0:index] = street_zero[0:index][::-1]
            else:
                result, rest = divmod(index - zero_old_ind, 2)
                street_zero[index - result:index] = street_zero[
                    zero_old_ind + 1:zero_old_ind + result + 1][::-1]
            zero_old_ind = index
        else:
            street_zero[index] = (index - zero_old_ind if zero_old_ind is not None else index + 1)
    return street_zero


def read_input() -> Street:
    """Ввод данных."""
    n = int(input())
    street = list(map(int, input().strip().split()))
    return street, n


if __name__ == '__main__':
    street, n = read_input()
    result = get_best_zero(street, n)
    print(*result)
