# A, B = map(int,input().split())
# C = int(input())

# if B + C >= 60:
#     A1 = (B+C) // 60
#     D = (B+C) % 60
#     E = A + A1
#     if E > 23:
#         E = E - 24
#     print(E, D)
    
# else:
#     print(A, B+C)
    

A, B = map(int, input().split())
C = int(input())

# 총 분 계산
total_minutes = B + C
A += total_minutes // 60  # 시간으로 증가
B = total_minutes % 60    # 분 업데이트

# 24시간 형식 유지
A %= 24

print(A, B)
