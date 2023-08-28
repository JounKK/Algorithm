system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
ans = ''

while N != 0:
    ans += str(system[N%B])
    N //= B

print(ans[::-1])