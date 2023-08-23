import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    phonebook = []

    for _ in range(n):
        phonebook.append(input().rstrip())

    phonebook.sort()
    flag = True

    for i in range(n-1):
        if phonebook[i] == phonebook[i+1][:len(phonebook[i])]:
            flag = False
            break

    print("YES") if flag else print("NO")