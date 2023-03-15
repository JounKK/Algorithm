total = int(input())
categories = int(input())

total_sum = 0
for n in range(categories):
    price, b = map(int, input().split())
    total_sum += price * b

if total_sum == total:
    print("Yes")
else: print("No")
