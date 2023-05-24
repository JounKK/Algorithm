def solution(n):
    three = []
    i = 1
    while(len(three) != n):
        if (i % 3 == 0) or (str(i).find('3') != -1):
            i += 1
        else:
            three.append(i)
            i += 1

    return three[-1]