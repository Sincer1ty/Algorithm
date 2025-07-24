import sys

input = sys.stdin.readline

N = int(input())
integer = list(map(int,input().split()))
v = int(input())
result = 0

for i in integer:
    if i == v:
        result += 1

print(result)
