# 돌면서 앞단어[-1] 현재단어[0] 이 같으면서 단어 길이 2이상
# 참여인원, 끝말잇기 정보

def solution(n, words):
    answer = []
    for i in range(1, len(words)):  # 1번일때 1번, 1번
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            # 탈락한 사람 번호, 탈락한 턴
            answer = [(i % n) + 1, (i // n) + 1]
            break
    if len(answer) == 0:
        answer = [0,0]
    return answer