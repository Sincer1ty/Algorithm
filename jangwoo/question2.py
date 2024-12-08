N = list(map(int,input().split()))

left_array = list(N)
right_array = []
answer = []

for i in range(len(N)):
    dif = sum(left_array)-sum(right_array)
    answer.append(abs(dif))   
    right_array.append(left_array.pop())

min_index = answer.index(min(answer))
left_array_size = len(N) - min_index

print(left_array_size)



