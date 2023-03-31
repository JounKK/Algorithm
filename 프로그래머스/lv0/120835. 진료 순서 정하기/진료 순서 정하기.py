def solution(emergency):
    # [3, 76, 24]를 [76, 24, 3]와 같이 정렬해서 이 정렬된 값에서 index(원본)을 해서 리턴합니다.
    응급순서 = sorted(emergency, reverse=True)
    return [응급순서.index(응급도)+1 for 응급도 in emergency]