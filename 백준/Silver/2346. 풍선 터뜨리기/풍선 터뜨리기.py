from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))
solution = []

for _ in range(n):
    idx, val = q.popleft()
    solution.append(idx + 1)
    
    if val > 0:
        q.rotate(-(val-1))
    else:
        q.rotate(-val)

print(' '.join(map(str, solution)))