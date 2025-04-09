class Solution(object):
    def minOperations(self, nums, k):

        # 배열에 k 보다 작은수가 있으면 -1 리턴
        if min(nums) < k:
            return -1
        # ----------------------------------
        count = 0

        # K도 리스트에 넣어주어야 모든 원소를 k로 바꿀 수 있음 아니면 리스트중 제일 작은 값으로만 바꿈
        unique = list(sorted(set(nums + [k]), reverse = True))
        for i in range(len(unique)):
            h = unique[i]

            # h보다 큰값 찾기
            big = []
            for j in nums:
                if j > h:
                    big.append(j)

            # 큰값 없음 넘기
            if len(big) == 0:
                continue
            # 큰값이 모두 같은가 확인
            if len(set(big)) != 1:
                return -1
            
            for k in range(len(nums)):
                if nums[k] > h:
                    nums[k] = h
            count += 1

        return count

                

        # h = unique[1]

        # for i in range(len(nums)):
        #     if nums[i] > h:
        #         nums[i] = h
        #         count += 1
        #     else:
        #         h = unique[count + 1]

        # return count
        