N = int(input())
for _ in range(N):
    score = 0
    cnt = 0
    quiz = input()
    for i in quiz:
        if i == 'O':
            cnt += 1
        else:
            cnt = 0
        score += cnt
        
    print(score)