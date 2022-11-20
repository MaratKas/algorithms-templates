LOCAL = True

if LOCAL:
    class Stack:
        def __init__(self):
            self.items = []
            self.cache = []

        def push(self, item):
            self.items.append(int(item))
            if self.cache:
                if item >= self.cache[-1]:
                    self.cache.append(item)
            else:
                self.cache.append(item)

        def pop(self):
            if len(self.items) > 0:
                if self.cache: 
                    if self.items[-1] == self.cache[-1]:
                        self.cache.pop()
                return self.items.pop()
            else:
                return print('error')
            
        def peek(self):
            return self.items[-1]

        def size(self):
            return len(self.items)

        def get_max(self):
            if self.items:
                return print(self.cache[-1])
                # return print(max(self.items))
            else:
                return print('None')


def solution(comnd):
    stack = Stack()
    for cmd in comnd:
        if cmd[0] == "get_max":
            stack.get_max()
        elif cmd[0] == "push":
            stack.push(int(cmd[1]))
        elif cmd[0] == "pop":
            stack.pop()


def read_input() -> list():
    n = int(input())
    comnd = [0] * n
    for i in range(n):
        # print(input().strip().split())
        # print(list(map(str, input().strip().split())))
        comnd[i] = input().split()
    return comnd


if __name__ == '__main__':
    comnd = read_input()
    solution(comnd)
