# Рита по поручению Тимофея наводит порядок в правильных скобочных последовательностях (ПСП), состоящих только из круглых скобок (). Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном порядке —– алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.
# Помогите Рите —– напишите программу, которая по заданному n выведет все ПСП в нужном порядке.

def gen_parentheses(n: int, m: int,  parentheses: str,):
    if n == 0 and m == 1:
        print(parentheses + ')')
    else:
        # print(str(n) + "- " + str(m))
        if n > 0:
            gen_parentheses(n - 1, m, parentheses + '(')
        if m > 1 and n < m:
            gen_parentheses(n, m - 1, parentheses + ')')


def read_input() -> int:
    n = int(input())
    return n


if __name__ == '__main__':
    n = read_input()
    gen_parentheses(n - 1, n, "(")
