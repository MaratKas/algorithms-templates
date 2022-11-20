from typing import List, Tuple
# ID 72945061

Keyboard = List[str]


def get_max_score(keyboard: Keyboard, fingers: int) -> int:
    """Проверка получения баллов."""
    keys = set(keyboard)
    score = 0
    for key in keys:
        if fingers * 2 >= keyboard.count(key) and key != ".":
            score += 1
    return score


def read_input() -> Tuple[int, str]:
    """Вводные данные."""
    fingers = int(input())
    keyboard = [input() for i in range(4)]
    return "".join(keyboard), fingers


if __name__ == '__main__':
    keyboard, fingers = read_input()
    print(get_max_score(keyboard, fingers))
