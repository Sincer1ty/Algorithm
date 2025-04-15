class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
    
        # nums2에서 각 값의 인덱스를 저장
        index_in_nums2 = {val: i for i, val in enumerate(nums2)}
    
        count = 0
    
        # nums1에서 i < j < k 조합을 모두 탐색
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c = nums1[i], nums1[j], nums1[k]
                    # nums2에서 a, b, c의 인덱스 순서도 오름차순이어야 함
                    if index_in_nums2[a] < index_in_nums2[b] < index_in_nums2[c]:
                        count += 1
                    
        return count