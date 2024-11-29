a = 2
b = 91

def solution(a, b):
    return max(int(f"{a}{b}"), 2 * a * b)

print(solution(a, b))

def solution2(a, b):
    return max(int(str(a)+str(b)), 2 * a * b)

print(solution2(a, b))