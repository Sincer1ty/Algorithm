# def solution(arr):
    
#     for i in arr:
#         print(i, end ='')
        
# 이렇게 하고 왜 안되지....하고 있었는데 문제가 문자열을 return하는 solution함수를 작성하는 거였네...

arr = ["a","b","c"]

def solution(arr):
    
    answer = ''
    for i in arr:
        answer += i
    
    return answer

print(solution(arr))

# 진짜 너무 어렵다...
# 근데 join()함수를 써도 엄청 쉽게 되는거 같은데

def solution(arr):
    return ''.join(arr)

print(solution(arr))

# 이렇게 두개다 잘 된다.
# 근데 ide에서 하면 print를 통해서 터미널에 띄워줘야하는구나
# return만 해놓고 왜 안되지...하고 있었는데 