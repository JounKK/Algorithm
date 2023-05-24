def solution(score):
    score_list = sorted([sum(x) for x in score], reverse=True)
    return [score_list.index(sum(j)) +1 for j in score]