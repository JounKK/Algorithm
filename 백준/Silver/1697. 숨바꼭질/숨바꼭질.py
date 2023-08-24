from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            print(visited[v])
            break
        for i in (v-1, v+1, v*2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[v] +1
                q.append(i)
        
MAX = int(1e5)                # 제한
visited = [0] * (MAX +1) # 방문차원 저장
n, k = map(int, input().split())

bfs()