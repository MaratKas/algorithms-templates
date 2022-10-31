from typing import List
# ID 72945061
Keyboard = List[int]


def get_max_score(keyboard: Keyboard, fingers: int) -> int:
    """Проверка получения баллов."""
    keys = []
    keys = set(keyboard)
    score = 0
    for key in keys:
        if fingers * 2 >= keyboard.count(key, 0, len(keyboard)) and key != ".":
            score += 1
    return score


def read_input() -> Keyboard:
    """Вводные данные."""
    fingers = int(input())
    keyboard = [input() for i in range(4)]
    return "".join(keyboard), fingers


if __name__ == '__main__':
    keyboard, fingers = read_input()
    print(get_max_score(keyboard, fingers))
