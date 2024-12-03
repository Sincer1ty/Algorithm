import sys
sys.setrecursionlimit(10**8)

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

vertex, edge = map(int, input().split())

parent = [0] * (vertex + 1)
edges = []
result = 0

for i in range(1, vertex + 1):
    parent[i] = i
    
for _ in range(edge):
    node1, node2, value = map(int, input().split())
    edges.append((value, node1, node2))
    
edges.sort()

for edge in edges:
    value, node1, node2 = edge
    if find_parent(parent, node1) != find_parent(parent, node2):
        union_parent(node1, node2)
        result += value
print(result)


    
