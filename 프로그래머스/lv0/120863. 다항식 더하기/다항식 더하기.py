def solution(입력값):
    항 = [0, 0] # x항, 일반항
    for i in 입력값.replace(' ','').split('+'):
        if 'x' in i:
            if len(i) == 1:
                항[0] += 1
            else:
                항[0] += int(i[:-1])
        else:
            항[1] += int(i)

    if 항[0] == 1 and 항[1] == 0:
        return f"x"
    if 항[0] == 1 and 항[1] != 0:
        return f"x + {항[1]}"

    if 항[0] == 0 and 항[1] == 0:
        return f""
    if 항[0] == 0 and 항[1] != 0:
        return f"{항[1]}"
    if 항[0] != 0 and 항[1] == 0:
        return f"{항[0]}x"
    if 항[0] != 0 and 항[1] != 0:
        return f"{항[0]}x + {항[1]}"