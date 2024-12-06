import sys
input = sys.stdin.readline

string = input().strip()

def postChar(string):
	idx = 0
	for i in range(len(string) - 1):
		if string[i] < string[i+1]:
			idx = i+1
	
	return idx

# 가장 뒤에 오는 문자의 인덱스 기준 슬라이스 반복
result = []
while string:
	idx = postChar(string)
	result.append(string[idx])
	string = string[idx+1:]

print(*result)
