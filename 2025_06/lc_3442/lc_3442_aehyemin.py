class Solution:
    def maxDifference(self, s: str) -> int:
        hash = {}
        odd = []
        even = []
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        val = hash.values()

        for j in val:
            if j % 2 != 0:
                odd.append(j)
            else:
                even.append(j)
        return max(odd) - min(even)