from collections import deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        #첫번째 트리 노드 n [0, n-1], 두번째 트리 노드개수m [0,m-1]
        #edges[i] = [a_i,b_i] 사이에 간선이 있다
        #target node = 두 노드 사이의 간선 수가 거리
        #첫번째 트리의 노드0으로부터의 노드5개 + 노드1로부
        #어떤 노드로부터 k이내에 속하는 노드들만 세기
        #두 트리를 연결하는 간선을 하나 추가해 트리를 이어줌, 최대가 되도록
        #1. edge1 처리
        #2. edge2 내부
        #3. edge2 최대값 처리
        n = len(edges1) + 1
        m = len(edges2) + 1
        edg1 = [[] for _ in range(n)]
        edg2 = [[] for _ in range(m)]
        for u,v in edges1:
            edg1[u].append(v)
            edg1[v].append(u)

        for u,v in edges2:
            edg2[u].append(v)
            edg2[v].append(u)

        #1. 첫번째 그래프 거리 <= k 인 노드 개수 구하기
        cnt1 = [0] * n
        for i in range(n):
            q = deque([i])
            distance = [-1] * n
            distance[i] = 0 #자신은 거리0
            cnt = 1 #자기자신포함
            while q:
                u = q.popleft()
                if distance[u] == k:
                    continue
                for j in edg1[u]:
                    if distance[j] == -1:
                        distance[j] = distance[u] + 1
                        cnt += 1
                        q.append(j)
            cnt1[i] = cnt

        #2. 두번째 그래프에서 거리<= k-1 인 노드개수 저장
        cnt2 = [0] * m
        if k == 0:
            max_cnt2 = 0
        else:
            for y in range(m):
                q = deque([y])
                distance = [-1] * m
                distance[y] = 0
                cnt = 1
                while q:
                    u = q.popleft()
                    if distance[u] == k-1:
                        continue
                    for w in edg2[u]:
                        if distance[w] == -1:
                            distance[w] = distance[u] + 1
                            cnt += 1
                            q.append(w)
                cnt2[y] = cnt
        max_cnt2 = max(cnt2)
        
        ans = [cnt1[i] + max_cnt2 for i in range(n)]     
        return ans
        
            
        