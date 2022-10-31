def to_binary(number: int) -> str:
    bit = ''
    if number == 0:
        bit = '0'
    else:
        while number > 0:
            bit = str(number % 2) + bit
            number = number // 2
    return bit

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
