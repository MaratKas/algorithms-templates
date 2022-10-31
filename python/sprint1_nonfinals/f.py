import re

def is_palindrome(line: str) -> bool:
    # str_line = "".join(re.split ('; |, | |: ', line)).lower()
    str_line = line.translate({ord(i): None for i in ' ;:!=,.'}).lower()
    # k = 0
    # n = len(str_line)
    line_str = str_line[::-1]
    if line_str == str_line:
        return True
    else:
        return False
    # for i in str_line:
    #     if k >= n/2: return True
    #     if i != str_line[n-k]: return False
    #     k += 1

print(is_palindrome(input().strip()))
