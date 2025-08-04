student = 31 * [False]

for _ in range(28):
    N = int(input())
    student[N] = True

for i in range(1,31):
    if student[i] == False:
        print(i)
