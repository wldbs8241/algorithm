# 손익분기점
# 고정비용 + 가변비용*물량 = 판매가격*물량

import sys

fix, change, sale = map(int, sys.stdin.readline().split())
# fix, change, sale = map(int, input().split())

if (sale-change) != 0:
    if fix/(sale-change) > 0:
        print(int(fix/(sale-change)+1))
    else:
        print(-1)
else:
    print(-1)