# 필터
# def solution(my_string):  
#     return ''.join(list(filter(lambda x:x not in 'aeiou', my_string)))

# replace
# def solution(my_string):
#     return my_string.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

# 정규표현식
import re 

def solution(my_string): 
    return re.sub(r'[aeiou]','',my_string)