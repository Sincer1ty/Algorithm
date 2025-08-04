N,M = map(int,input().split())
bucket = [i for i in range(1,N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    
    sub = bucket[i-1:j]
    sub.reverse()
    bucket[i-1:j] = sub
    
print(*bucket)