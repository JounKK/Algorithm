import sys
input = sys.stdin.readline
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
 
class Trie:
    def __init__(self):
        self.head = Node(None)
 
    def insert(self, string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
 
        current_node.data = string
 
    def search(self, string):
        current_node = self.head
        for char in string:
            current_node = current_node.children[char]
 
        if current_node.children:
            return False
        else:
            return True    
 
for _ in range(int(input())):
    n = int(input())
    trie = Trie()
    phone = []
    for _ in range(n):
        w = input().rstrip()
        phone.append(w)
        trie.insert(w)
    
    res = True
    phone.sort()
    for p in phone:
        if not trie.search(p):
            res = False
            break
    if res:
        print("YES")
    else:
        print("NO")