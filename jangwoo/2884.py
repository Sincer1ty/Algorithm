# H, M = map(int,input().split())

# if M < 45:
#     if H == 0:
#         H = 23
#     else:
#         H = H - 1
#     M = M + 15
# else:
#     M = M - 45

# print(H, M)


H, M = map(int,input().split())

M = M - 45

if M < 0:
    if H == 0:
        H = 23
    else:
        H = H - 1
    M += 60

print(H, M)