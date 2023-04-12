def solution(age):
    행성 = 'abcdefghij'
    return ''.join(map(lambda x : 행성[int(x)], str(age)))