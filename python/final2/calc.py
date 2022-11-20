# 75288297
class Stack:
    """Клас стек-данных."""
    def __init__(self):
        self._items = []
        self.size = 0

    def push(self, item: int):
        self._items.append(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return print('error')
        self.size -= 1
        return self._items.pop()


def calc(calc_cmd: list) -> int:
    """Выполнение команд на калькуляторе."""
    operators = {
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x,
        '-': lambda x, y: y - x,
        '+': lambda x, y: x + y,
    }
    stack_arg = Stack()
    for arg in calc_cmd:
        if arg in operators:
            stack_arg.push(operators[arg](stack_arg.pop(), stack_arg.pop()))
        else:
            stack_arg.push(int(arg))
    return(stack_arg.pop())


if __name__ == '__main__':
    calc_cmd = input().split()
    result = calc(calc_cmd)
    print(result)
