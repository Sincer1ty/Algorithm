# my_string = "string"
# k = 3
# my_string = "love"
# k = 10

def solution(my_string, k):
    
    return my_string * int(k)

print(solution(my_string, k))

# 처음에는 my_string을 k번 만큼 반복을 돌려 그 친구를 answer = ''이라는 곳에 저장을 해 놓아야하나 생각했는데...
# 그냥 my_string에 k곱하면 되지 않을까 하고 했는데.. 되버리네