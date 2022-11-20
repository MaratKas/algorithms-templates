
class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size_len = 0

    def is_empty(self):
        return self.size_len == 0

    def push(self, x):
        if self.size_len != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size_len += 1
        else:
            print("error")

    def pop(self):
        if self.is_empty():
            print("None")
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size_len -= 1
            print(x)

    def peek(self):
        if self.is_empty():
            print("None")
        else:
            print(self.queue[self.head])

    def size(self):
        print(self.size_len)


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    queue = MyQueueSized(n)

    for _ in range(m):
        cmd = input().split()
        cd = cmd[0]
        if cd == "peek":
            queue.peek()
        elif cd == "push":
            queue.push(int(cmd[1]))
        elif cd == "pop":
            queue.pop()
        elif cd == "size":
            queue.size()
