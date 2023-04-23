from collections import deque

def solution(A, B):
    for i in range(len(A)):
        a = deque(A)
        a.rotate(i)
        if ''.join(a) == B:
            return i

    return -1