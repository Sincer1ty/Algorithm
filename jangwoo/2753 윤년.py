import sys
input = sys.stdin.readline

N = int(input())

if(N % 4 == 0 and N % 100 != 0):
    # 이때도 윤년
    print(1)
elif(N % 400 == 0):
    print(1)
else:
    print(0)


