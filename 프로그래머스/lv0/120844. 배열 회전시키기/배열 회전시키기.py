from collections import deque

def solution(numbers, direction):
    numbers_deque = deque(numbers)
    d = (1 if direction == 'right' else -1)
    numbers_deque.rotate(d)
    
    return list(numbers_deque)