def solution(price, money, count):
    
    fee = 0
    for i in range(1, count+1):
        fee += price * i
    
    if fee < money:
        answer = 0
    else:
        answer = fee - money
    
    return answer