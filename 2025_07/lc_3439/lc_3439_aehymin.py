class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        #[시작시간1, 끝나는시간1],  [시작시간2, 끝나는시간2]
        #회의는 겹치지 않음
        #회의를 k번 만큼 옮길 수 있다. 순서는 그대로 유지
        #연속된 가장 빈 시간을 반환
        #힌트1: k개의 회의, k+1 개의 gap. k개의 회의를 앞으로 옮길수 있으면 가장 긴 free time
        #힌트2: k+1의 갭을 대상으로 슬라이딩 윈도우 사용

        #인접한 회의k개를 선택해서 앞으로 붙인다
        #전체 구간길이에서 회의시간을 뺀다
        n = len(startTime) #전체 회의 개수
        ans = 0 #최대 자유시간
        t = 0 #현재 슬라이딩 윈도우 길이

        for i in range(n):
            t += endTime[i] - startTime[i]


            if i <= k-1:
                left = 0 #블록 맨 앞이면 0부터 시작하기
            else:
                left = endTime[i-k] #블록 바로 앞 회의의 끝 시간부터

            
            if i == n-1:
                #앞으로 당길 회의의 오른쪽 끝 경계
                right = eventTime 
            else:
                #뒤에 회의가 더 있을때
                right = startTime[i+1] #다음회의시작시간

            free = right - left - t
            ans = max(ans, free)

            #k개의 회의 길이 합 유지
            if i >= k-1:
                t -= endTime[i-k+1] - startTime[i-k+1]
        return ans









        