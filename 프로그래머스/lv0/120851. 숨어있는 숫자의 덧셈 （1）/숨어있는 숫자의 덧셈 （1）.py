import re

def solution(my_string):
    num = re.sub(r'[^0-9]','',my_string)
    return sum(map(int, num))