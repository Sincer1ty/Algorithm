from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 시작일 기준 정렬
        events.sort(key=lambda x: x[0])
        
        total = len(events)
        i = 0               # events 인덱스
        attended = 0        # 답
        day = 0
        pq = []             # 진행 중 행사들의 종료일 최소 힙
        
        # 모든 행사를 처리할 때까지 반복
        while i < total or pq:
            # 힙이 비어 있으면 다음 행사의 시작일로 day 점프
            if not pq and day < events[i][0]:
                day = events[i][0]
            
            # 오늘(day) 시작하는 모든 행사를 힙에 넣기
            while i < total and events[i][0] == day:
                heapq.heappush(pq, events[i][1])
                i += 1
            
            # 오늘 참석할 행사 선택 (종료일이 가장 빠른 것)
            if pq:
                heapq.heappop(pq)
                attended += 1
                day += 1  # 다음 날로 이동
            
            # 이미 끝난 행사 제거
            while pq and pq[0] < day:
                heapq.heappop(pq)
        
        return attended
