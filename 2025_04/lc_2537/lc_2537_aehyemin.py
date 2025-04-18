class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        #(i, j) i<j 이고 arr[i] == arr[j] k 페어
        #같은 값이 등장하는 인덱스 쌍이 k 이상이면 good
        #예시 1은 5C2 이다.
        #슬라이딩 윈도우, 해시맵
        hash = {}
        pair = 0
        left = 0
        ans = 0

        for i in range(len(nums)):

            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                pair += hash[nums[i]]
                hash[nums[i]] += 1

            while pair >= k:
                ans += len(nums) - i
                y = nums[left]
                hash[y] -= 1
                pair -= hash[y]

                left += 1

        return ans
