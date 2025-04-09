from collections import deque
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        numQueue = deque(nums)
        while len(numQueue) > 0:
            if len(set(numQueue)) == len(numQueue):
                return count
            for _ in range(min(3,len(numQueue))):
                numQueue.popleft()
            count += 1
        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]))
