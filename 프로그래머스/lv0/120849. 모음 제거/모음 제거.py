def solution(my_string):  
    return ''.join(list(filter(lambda x:x not in 'aeiou', my_string)))