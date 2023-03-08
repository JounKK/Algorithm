A, B = map(int, input().split())
C = int(input())

T = A * 60 + B
F = T + C

if F // 60 > 23:
    a = (F // 60) - 24
else:
    a = F // 60

b = F % 60

print(a, b)