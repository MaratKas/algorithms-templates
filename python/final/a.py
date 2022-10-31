from typing import List
# ID 72847757
Street = List[int]


def get_best_zero(street: Street, n: int) -> Street:
    """Постройка карты с растоянием до пустых участков."""
    street_zero = list(range(1, n + 1, 1))
    sample = list(range(0, n, 1))
    zero_old_ind = 0

    for index, element in enumerate(street, 0):
        if element == 0:
            if index == 0:
                street_zero = sample.copy()
            else:
                if zero_old_ind != 0:
                    street_zero[zero_old_ind:index+1] = sample[
                        :index - zero_old_ind + 1
                        ].copy()
                if index - zero_old_ind > 1:
                    if zero_old_ind > 0 or street_zero[0] == 0:
                        zero_old_ind += (index - zero_old_ind)//2 + 1
                    street_zero[zero_old_ind:index+1] = sample[
                        index - zero_old_ind::-1
                        ].copy()
                zero_old_ind = index
    if street[zero_old_ind] == 0:
        street_zero[zero_old_ind:index+1] = sample[
            :index - zero_old_ind + 1
            ]
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
