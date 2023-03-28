a_list = []
b_list = []
while True:
    a, b = map(int, input().split())
    if a+b == 0:
        break
    else: 
        a_list.append(a)
        b_list.append(b)
        
for i in range(len(a_list)):
    print(a_list[i] + b_list[i])
