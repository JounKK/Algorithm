def solution(numbers):
    return list(map(lambda x:x*2, numbers))

# 다차원이어도 가능한 해결법 (numpy는 행렬 연산도 가능)
# import numpy as np

# def solution(numbers):
#     numbers = np.array(numbers)
#     return (numbers * 2).tolist()