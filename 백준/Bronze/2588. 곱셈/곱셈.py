#2588
aaa = int(input())
bbb = int(input())

for b in str(bbb)[::-1]:
    print(aaa*int(b))
print(aaa*bbb)