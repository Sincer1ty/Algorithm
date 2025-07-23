eyes = list(map(int, input().split()))

if eyes[0] == eyes[1] == eyes[2]:
    print(10000 + eyes[0] * 1000)
elif eyes[0] == eyes[1] or eyes[0] == eyes[2]:
    print(1000 + eyes[0] * 100)
elif eyes[1] == eyes[2]:
    print(1000 + eyes[1] * 100)
else:
    print(max(eyes) * 100)