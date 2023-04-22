def solution(spell, dic):
    new = []
    for word in dic:
        if set(spell) - set(word) == set():
            new.append(word)
    return 1 if len(new) >= 1 else 2



