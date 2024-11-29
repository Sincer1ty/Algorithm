a = 9
b = 91

def solution(a, b):
    
    sum_str1 = str(a) + str(b)
    sum_str2 = str(b) + str(a)
    
    c = int(sum_str1)
    d = int(sum_str2)
    
    if c > d:
        return c
    else :
        return d
    

print(solution(a, b))



def solution2(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))

print(solution2(a, b))

def solution3(a, b):
    
    sum_str1 = str(a) + str(b)
    sum_str2 = str(b) + str(a)
    
    c = int(sum_str1)
    d = int(sum_str2)
    
    return max(c,d)
    

print(solution3(a, b))
