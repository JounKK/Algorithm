a, b, c = map(int, input().split())

if (a==b) & (b==c):
    prize = 10000 + a * 1000
elif (a==b) | (a==c):
    prize = 1000 + a *100
elif b==c:
    prize = 1000 + b *100
elif (a > b) & (a > c):
    prize = a * 100
elif (a < b) & (b > c):
    prize = b * 100
elif (a < c) & (b < c):
    prize = c * 100

print(prize)
