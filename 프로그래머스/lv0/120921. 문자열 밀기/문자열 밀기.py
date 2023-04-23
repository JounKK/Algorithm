from collections import deque

def solution(A, B):
    for i in range(len(A)):
        a = deque(A)
        a.rotate(i)
        if ''.join(a) == B:
            return i

    return -1


# 다른 답
# 2개를 이어붙여서 찾아보면 됨
# 회전형태로 돌아가는 것을 1차원 배열로 만들어서 인덱스를 찾는 방법
# 2차원으로 풀어야하는 것을 1차원으로 축소시켜서 푸는 방법 !
def solution1(A, B):
    return (B*2).find(A)

solution1("hellzo", "ohell")

