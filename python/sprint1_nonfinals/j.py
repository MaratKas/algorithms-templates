from typing import List

from typing import List

def factorize(number: int) -> List[int]:
    resul = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            resul.append(i)
            number = number/i
        else:
            i += 1
    resul.append(int(number))
    return resul


result = factorize(int(input()))
print(" ".join(map(str, result)))
