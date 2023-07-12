# 백준 1259 팰린드롬 수

while True:
    word = str(input())
    b = "".join(reversed(word))
    if word == '0':
        break
    elif word == b:
        print('yes')
    else:
        print('no')
