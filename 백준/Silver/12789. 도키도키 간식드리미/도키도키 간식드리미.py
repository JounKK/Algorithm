from collections import deque

n = int(input())
que = deque(map(int, input().split()))
stack = deque()
ord = 1

while que:
    if que[0] != ord:
        stack.append(que.popleft())

    else:
        que.popleft()
        ord += 1

    while stack and stack[-1] == ord:
        stack.pop()
        ord += 1

print("Nice" if not stack else "Sad")