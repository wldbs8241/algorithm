# 이름에 해당하는 그리움 점수는 모두 제공,
# photo에 담기는 리스트별로 그리움 점수 합산하기 

def solution(name, yearning, photo):
    answer = []
    for arr in photo:
        print(arr)
        res = 0
        for i in range(len(name)):
            print(i)
            if name[i] in arr:
                res += yearning[i]
        answer.append(res)
    return answer

