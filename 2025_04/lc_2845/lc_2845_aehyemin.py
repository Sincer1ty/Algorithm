class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        #흥미로운 하위 배열의 개수 찾기
        # nums[i] % modulo == k인 원소의 개수를 cnt라고 할 때,
        # cnt % modulo == k 조건을 만족
        dict = {0:1}
        cnt = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                cnt += 1
            #cnt = prefix_cnt[r] - prefix_cnt[l-1]
            #cnt % modulo == k
            #(prefix_cnt[r] - prefix_cnt[l-1]) % modulo == k
            #prfix_cnt[r] % modulo = (prefix_cnt[l-1] + k ) % m
            t = (cnt - k) % modulo
            ans += dict.get(t, 0)
            cur = cnt % modulo
            dict[cur] = dict.get(cur, 0) + 1
        return ans    