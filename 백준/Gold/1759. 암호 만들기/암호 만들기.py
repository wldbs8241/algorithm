# 포함이 되느냐 마느냐
def backtrack(len, start):
# 종료조건
    if len == L:        # 만든 암호의 길이가 주어진 길이와 같다면
        con, vo = 0, 0  # 일단 자음, 모음 카운트 초기화시키기

        for i in range(L):      # 주어진 암호 길이 만큼 돌면서
            if res[i] in 'aeiou':   # 결과 암호에 모음 카운드
                vo += 1
            else:
                con += 1
        if vo >= 1 and con >= 2:
            print(*res, sep='')

    for j in range(start, C):
        if visit[j] == 0:
            res.append(words[j])
            visit[j] = 1
            backtrack(len+1, j+1)   # 한줄기 포함할 때
            visit[j] = 0    # 다음 암호 출력에 방해되지 않게 다시 리셋해주기
            del res[-1]     # 포함시킨 알파벳을 제거해준다. 중복 x


L, C = map(int, input().split())
words = input().split()
words.sort()
visit = [0 for _ in range(C)]
res = []
backtrack(0, 0)