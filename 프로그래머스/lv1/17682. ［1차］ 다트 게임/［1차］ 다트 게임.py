def solution(dartResult):
    result = []
    for index, value in enumerate(dartResult):
        if value == 'S':
            result[-1] **= 1
        elif value == 'D':
            result[-1] **= 2
        elif value == 'T':
            result[-1] **= 3
        
        # 스타상 처리
        elif value == '*':
            result[-1] *= 2
            if len(result) >= 2:
                result[-2] *= 2
        
        elif value == '#':
            result[-1] *= -1
        else:
            if dartResult[index:index+2] == '10':
                result.append(10)
            elif dartResult[index-1:index+1] != '10':
                result.append(int(value))
    return sum(result)