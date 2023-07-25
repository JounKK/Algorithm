# 문제 링크 : https://codingdojang.com/scode/408

# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
# 예를들어 S= [1, 3, 4, 8, 13, 17, 20] 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.

# 풀이
# 2번째 - 1번째
# 가장 작은 값을 무한대로 설정하고, 차이 비교 하면서 index 저장

S= [1, 3, 4, 8, 13, 17, 20]

index = 0 
min = float('inf')
for i in range(1, len(S)):
    if (S[i] - S[i-1]) < min:
        index = i
        min = S[i] - S[i-1]
    
S[index - 1], S[index]
