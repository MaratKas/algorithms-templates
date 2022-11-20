
class MyQueueSized:
    def __init__(self):
        self.queue = []
        self.size_len = 0

    def is_empty(self):
        return self.size_len == 0

    def put(self, item):
        self.size_len += 1
        self.queue.append(int(item))

    def get(self):
        if self.is_empty():
            print("error")
        else:
            self.size_len -= 1
            print(self.queue.pop(0))

    def size(self):
        print(self.size_len)


if __name__ == '__main__':
    m = int(input())
    queue = MyQueueSized()

    for _ in range(m):
        cmd = input().split()
        cd = cmd[0]
        if cd == "get":
            queue.get()
        elif cd == "put":
            queue.put(int(cmd[1]))
        elif cd == "size":
            queue.size()
