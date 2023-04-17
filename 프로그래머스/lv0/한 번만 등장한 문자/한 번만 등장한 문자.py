def solution(s):
    return ''.join(sorted([st for st in s if s.count(st) == 1]))
