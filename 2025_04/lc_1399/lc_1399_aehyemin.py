class Solution:
    def countLargestGroup(self, n: int) -> int:
        #1부터 n까지의 각 숫자는 그 숫자의 합에 따라 그룹화된다.
        #가장 큰 크기를 가진 그룹의 수를 반환합니다
        #그 수의 자릿수의 합
        #1:[1,10] 2:[2,11], 3:[3,12], 4:[4,13], 5:[5], [6], [7], [8], [9], [10],
        cnt = [0] * 37
        ans = 0
        
        for i in range(1, n+1):
            cur = i
            x = 0
            while cur > 0:
                x += cur % 10 # x += 123 % 10 = 3
                cur = cur // 10 # 12
            cnt[x] += 1

        max_num = max(cnt)
        for k in cnt:
            if k == max_num:
                ans += 1
        return ans

            