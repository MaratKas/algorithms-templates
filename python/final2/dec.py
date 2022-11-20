# 75206062
class MyDeque:
    """
    Клас ДЕК.

    push_back(value) – добавить элемент в конец дека.
    push_front(value) – добавить элемент в начало дека.
    pop_front() – вывести первый элемент дека и удалить его.
    pop_back() – вывести последний элемент дека и удалить его.
    """
    def __init__(self, size_queue):
        self._deque = [None] * size_queue
        self.max_n = size_queue
        self.head = 0
        self.tail = 1
        self.lengs = 0

    def is_empty(self):
        return self.lengs == 0

    def push_back(self, item):
        if self.lengs == self.max_n:
            raise Exception("error")
        self._deque[self.tail] = item
        self.tail = get_index(self.tail, True, self.max_n)
        self.lengs += 1

    def push_front(self, item):
        if self.lengs == self.max_n:
            raise Exception("error")
        self._deque[self.head] = item
        self.head = get_index(self.head, False, self.max_n)
        self.lengs += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise Exception("error")
        self.head = get_index(self.head, True, self.max_n)
        item = self._deque[self.head]
        self._deque[self.head] = None
        self.lengs -= 1
        return(item)

    def pop_back(self) -> int:
        if self.is_empty():
            raise Exception("error")
        self.tail = get_index(self.tail, False, self.max_n)
        item = self._deque[self.tail]
        self._deque[self.tail] = None
        self.lengs -= 1
        return(item)


def get_index(index: int, sign: bool, max_n) -> int:
    """Поиск индекса для ДЕК"""
    if sign:
        return (index + 1) % max_n
    else:
        return (index - 1) % max_n


if __name__ == '__main__':
    amount_cmd = int(input())
    size_deque = int(input())
    deque = MyDeque(size_deque)
    for _ in range(amount_cmd):
        cmd, *arg = input().split()
        try:
            rezult = getattr(deque, cmd)(
                int(arg[0])
                ) if arg else getattr(deque, cmd)()
            if rezult is not None:
                print(rezult)
        except Exception as error:
            print(error)
