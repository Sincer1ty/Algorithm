class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        res = n
        for i in fruits:
            for j in range(n):
                if i <= baskets[j]:
                    res -= 1
                    baskets[j] = 0
                    break
        return res

