def get_longest_word(line: str) -> str:
    lst = line.split()
    # sort_lst = sorted(lst, key=len)
    return max(lst, key=len)

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
