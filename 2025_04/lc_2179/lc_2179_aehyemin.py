class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        one = {}
        two = {}
        n = len(nums1)
        for i in range(n):
            one[nums1[i]] = i

        for i in range(n):
            two[nums2[i]] = i

        total = 0
        
        for y in range(n):
            pos1 = one[y] #인덱스에 따른 값
            pos2 = two[y]
            
            x_cnt = 0
            z_cnt = 0
            
            for x in range(n):
                if y == x:
                    continue
                if pos1 > one[x] and pos2 > two[x]:
                    x_cnt += 1

            for z in range(n):
                if y == z:
                    continue
                if one[z] > pos1 and two[z] > pos2:
                    z_cnt += 1
            total += x_cnt * z_cnt
        return total
