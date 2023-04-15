# def solution(before, after):
#     for i in before:
#         after = after.replace(i,'',1)

#     if len(after) == 0:
#         return 1
#     else:
#         return 0
    
# 더 쉽게 푸는 법 : 정렬
def solution(before, after):
    return 1 if sorted(list(before)) == sorted(list(after)) else 0