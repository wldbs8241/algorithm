# 10개씩 끊어 출력하기

words = input()
N = len(words)

for i in range(0, N, 10):
    print(words[i:i+10])