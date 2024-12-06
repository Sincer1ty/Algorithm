import sys
input = sys.stdin.readline

seq1 = input().strip()
seq2 = input().strip()

len1 = len(seq1)
len2 = len(seq2)
matrix = [[0]*(len1+1) for _ in range(len2+1)]

for i in range(1, len2+1):
	for j in range(1, len1+1):
		if seq1[j-1] == seq2[i-1]:
			matrix[i][j] = matrix[i-1][j-1] + 1
		else:
			matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[len2][len1])

i = len2
j = len1
result = []
while i != 0 and j != 0 :
	if matrix[i][j] == matrix[i-1][j]:
		i -= 1
	elif matrix[i][j] == matrix[i][j-1]:
		j -= 1
	else:
		result.append(seq1[j-1])
		i -= 1
		j -= 1

result.reverse()
for r in result:
	print(r, end="")
