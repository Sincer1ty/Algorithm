remain = set()

for _ in range(10):
    N = int(input())
    if N % 42 not in remain:
        remain.add(N%42)
          
print(len(remain))
