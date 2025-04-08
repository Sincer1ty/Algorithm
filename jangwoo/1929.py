import sys
input = sys.stdin.readline

def combination(selected_count,idx):
    if selected_count == 6:
        print(*selected_numbers)
        return

    for i in range(idx,total_numbers): # 0~7 -> 1~7 -> 2,7 ... ->5,7
        selected_numbers.append(input_numbers[i])
        combination(selected_count + 1, i + 1)
        selected_numbers.pop()
    return

while True:
    array = list(map(int,input().split()))
    total_numbers = array[0]
    
    if total_numbers == 0:
        break
    
    input_numbers = array[1:]
    selected_numbers = []
    
    combination(0,0)
    
    print()