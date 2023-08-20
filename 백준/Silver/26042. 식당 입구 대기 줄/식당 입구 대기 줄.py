import sys
input = sys.stdin.readline

A = []
n = int(input())
max = [0, 0]

for _ in range(n):
    cmd = input().split()
    if cmd[0] == '1':
        A.append(int(cmd[1]))
    elif cmd[0] == '2':
        A.pop(0)

    if max[0] < len(A):
        max[0] = len(A)
        max[1] = A[-1]
    elif max[0] == len(A):
        max[1] = min(max[1], A[-1])

print(max[0], max[1])