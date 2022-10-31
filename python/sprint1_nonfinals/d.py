# Хаотичность погоды
from typing import List

def get_weather_randomness(temperatures: List[int], n: int) -> int:
    if n == 1:
        return 1
    else:
        house = 0
        if (temperatures[0] > temperatures[1]):
            house += 1
        if (temperatures[n-1] > temperatures[n-2]):
            house += 1
        for i in range(1, n-1):
            if (temperatures[i-1] < temperatures[i]) and (temperatures[i] > temperatures[i+1]):
                house += 1
                i += 1
                continue
        return house

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures, n

temperatures, n = read_input()
print(get_weather_randomness(temperatures, n))
