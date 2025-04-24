class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n < 10:
            return n

        count = {}

        for i in range(1, n + 1):
            lenSum = 0
            j = i
            while j > 0:
                lenSum += j%10
                j = j//10
            count[lenSum] = count.get(lenSum, 0) + 1
        maxSize = max(count.values())

        maxSizeGroups = 0
        for i in count.values():
            if i == maxSize:
                maxSizeGroups += 1
        return maxSizeGroups
