import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Deque:

    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init

        self.현재노드 = None
        self.데이터수 = 0

    def push_front(self, data):
        새로운노드 = Node(data)
        새로운노드.next = self.head
        self.head = 새로운노드
        self.데이터수 += 1
        if self.데이터수 == 1:
            self.tail = 새로운노드

    def push_back(self, data):
        새로운노드 = Node(data)
        self.tail.next = 새로운노드
        self.tail = 새로운노드
        self.데이터수 += 1
        if self.데이터수 == 1:
            self.head = 새로운노드

    def pop_front(self):
        if self.데이터수 == 0:
            return -1
        data = self.head.data
        self.head = self.head.next
        self.데이터수 -= 1
        return data

    def pop_back(self):
        if self.데이터수 == 0:
            return -1

        data = self.tail.data
        현재노드 = self.head

        for i in range(self.데이터수):
            if 현재노드.next is self.tail:
                self.tail = 현재노드
                break
            현재노드 = 현재노드.next

        self.데이터수 -= 1
        return data

    def size(self):
        return self.데이터수

    def empty(self):
        return 1 if self.데이터수 == 0 else 0
    
    def front(self):
        if self.데이터수 == 0:
            return -1
        return self.head.data

    def back(self):
        if self.데이터수 == 0:
            return -1
        return self.tail.data
    
    
n = int(input())
d = Deque()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push_back':
        d.push_back(int(cmd[1]))
    elif cmd[0] == 'push_front':
        d.push_front(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        print(d.pop_front())
    elif cmd[0] == 'pop_back':
        print(d.pop_back())
    elif cmd[0] == 'size':
        print(d.size())
    elif cmd[0] == 'empty':
        print(d.empty())
    elif cmd[0] == 'front':
        print(d.front())
    elif cmd[0] == 'back':
        print(d.back())
