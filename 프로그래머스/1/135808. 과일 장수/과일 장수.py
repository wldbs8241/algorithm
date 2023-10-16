# k는 최대 점수
# m은 사과상자에 들어가는 사과 갯수
# 사과상자의 가격 = 가장 낮은 사과 점수 x 사과개수
# 사과는 상자 단위로만 판매 가능
# 최대이익을 구하기 위해서 가격이 높은 순서대로 커트하기

# def solution(k, m, score):
#     answer = 0
#     while len(score) >= m:
#         score.sort(reverse=True)
#         price = score[0:m]
#         answer += min(price)*m    
#         del score[0:m]
#     return answer

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m):
        # 0123, 4567, 891011
        appleBox = score[m*i:m*(i+1)]
        answer += appleBox[-1]*m
    return answer
    