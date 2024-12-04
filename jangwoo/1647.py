import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:   
        parent[b] = a
    else:
        parent[a] = b

home , road = map(int, input().split())

parent = [0] * (home + 1)
edges = []
result = 0
last_edge = 0 


for i in range(1, home + 1):
    parent[i] = i
    
for _ in range(road):
    a, b, c = map(int,input().split())
    edges.append((c, a, b))
edges.sort()

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(a,b)
        result += c # 간선 비용을 result에 더함
        last_edge = c # 마지막 추가된 간선이 cost가 가장 큰 간선, 두 트리로 나누는 과정에서 제외.
        
print(result - last_edge)

