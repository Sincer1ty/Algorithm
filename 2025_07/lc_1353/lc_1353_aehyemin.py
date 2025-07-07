class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        max_day = max(i[1] for i in events)
        #시작시간순으로 정렬
        #시작시간 같은데 끝나는 시간 다르면 종료시간 기준 오름차순
        q = []
        j = 0
        ans = 0
        for i in range(1, max_day+1): #1일차부터 마지막까지
            while j < n and events[j][0] <= i:
                heapq.heappush(q, events[j][1]) 
                #오늘날짜에 시작하는 이벤트 힙에 전부 추가
                #힙큐 자동정렬
                j += 1
             
            while q and q[0] < i: #오늘날짜보다 이미 끝난 이벤트 제거
                heapq.heappop(q)

            if q:
                heapq.heappop(q)
                ans += 1

        return ans

        
        