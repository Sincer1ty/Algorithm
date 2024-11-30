A, B = map(int,input().split())
C = int(input())

if B + C >= 60:
    A1 = (B+C) // 60
    D = (B+C) % 60
    E = A + A1
    if E > 23:
        E = E - 24
    print(E, D)
    
else:
    print(A, B+C)
    
# 아 또 김성희 도움 받았다.아!~!!!!