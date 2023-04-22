def solution(spell, dic):
    new = []
    for word in dic:
        if set(spell) - set(word) == set():
            new.append(word)
    return 1 if len(new) >= 1 else 2


# 강사님 답
# sorted(스트링단어) > 한자씩 리스트 정렬된다. 
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
        
    return 2
