s = input()

result = []
max_char =''

for char in reversed(s):
    if char >= max_char:
        max_char = char
        result.append(char)

print(''.join(reversed(result)))
