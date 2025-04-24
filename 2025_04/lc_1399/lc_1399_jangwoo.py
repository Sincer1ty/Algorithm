class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = [0] * 37 # 해당 자리수 합을 가진 숫자 갯수
        ans = 0 # 가장 큰 크기 그룹의 개수

        for i in range(1 , n + 1):
            ans = 0 # 가장 긴 완전 부분 집합의 개수를 기록
            x = i
            while x:
                ans += x % 10
                x //= 10
            cnt[ans] += 1
        
        largest_group = max(cnt)
        return cnt.count(largest_group)