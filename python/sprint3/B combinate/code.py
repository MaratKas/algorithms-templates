
Keybord = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

result = []


def gen_letter_variants(n: str, letter: str, result: str):
    if len(n) < 1:
        result.append(letter)
    else:
        number = list(n).pop(0)
        for key in list(Keybord[int(number)]):
            result = gen_letter_variants(n[1:], letter + key, result)
    return result


def read_input() -> str:
    n = input()
    return n


if __name__ == '__main__':
    n = read_input()
    result = gen_letter_variants(n, "", result)
    print(' '.join(result))
