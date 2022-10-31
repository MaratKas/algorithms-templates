from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    l_f = len(first_number)
    l_s = len(second_number)
    sum_bit = ""
    delta = 0
    for i in range(1, max(l_f, l_s)+1):
        rez = 0
        rez += delta
        if l_f >= i:
            rez += int(first_number[-i])
        if l_s >= i:
            rez += int(second_number[-i])
        if rez == 0:
            sum_bit += "0"
            delta = 0
        elif rez == 1:
            sum_bit += "1"
            delta = 0
        elif rez == 2:
            sum_bit += "0"
            delta = 1
        elif rez == 3:
            sum_bit += "1"
            delta = 1
    if delta == 1:
        sum_bit += "1"
    return sum_bit[::-1]

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
