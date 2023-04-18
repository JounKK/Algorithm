# def solution(my_str, n):
#     return [my_str[i:i+n] for i in range(0, len(my_str), n)]

# 정규표현식
import re
def solution(my_str, n):
    p = re.compile(f'.{{1,{n}}}')
    return p.findall(my_str)