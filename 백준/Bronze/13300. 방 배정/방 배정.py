# 방배정
N, M = map(int, input().split())    # N: 총 학생 수 M:방별 최대 인원
w_cnt = [0 for _ in range(6)]       # 여학생 학년별로 필요한 방 리스트
m_cnt = [0 for _ in range(6)]       # 남학생 학년별로 필요한 방 리스트
res = [0 for _ in range(6)]         # 최종적으로 필요한 방 카운트
for _ in range(N):
    S, G = map(int, input().split())
    if S == 0:      # 학생이 여자일때
        for i in range(1, 7):
            if G == i:
                w_cnt[i-1] += 1
    else:
        for i in range(1, 7):
            if G == i:
                m_cnt[i-1] += 1

for room in range(6):
    if w_cnt[room] % M == 0:
        res[room] += w_cnt[room]//M
    elif w_cnt[room] // M == 0:
        res[room] += 1
    else:
        res[room] += w_cnt[room]//M + 1

for room in range(6):
    if m_cnt[room] % M == 0:
        res[room] += m_cnt[room]//M
    elif m_cnt[room] // M == 0:
        res[room] += 1
    else:
        res[room] += m_cnt[room]//M + 1

print(sum(res))