# def solution(order):
#     count = 0
#     count += str(order).count('3')
#     count += str(order).count('6')
#     count += str(order).count('9')
#     return count

# 정규표현식
import re

def solution(order):
    return len(re.findall('[369]', str(order)))