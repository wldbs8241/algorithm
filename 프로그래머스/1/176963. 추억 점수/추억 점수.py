# 이름에 해당하는 그리움 점수는 모두 제공,
# photo에 담기는 리스트별로 그리움 점수 합산하기 

def solution(name, yearning, photo):
    answer = []
    for arr in photo:
        print(arr)
        score = 0
        for num in range(len(name)):
            # print(num)
            if name[num] in arr:
                score += yearning[num]
        answer.append(score)
    return answer

