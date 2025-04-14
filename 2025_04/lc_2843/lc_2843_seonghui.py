class Solution:
    def makePowerOfTwo(self, n):
        # 홀수이면 안 됨
        if n == 1:
            return 2
        # 이미 2의 제곱수
        elif (n & (n - 1)) == 0:
            return n

        power = 1
        while power < n:
            power <<= 1
        return power
        
    def find_combinations(self, total):
        result = []
        for a in range(total + 1):
            for b in range(total + 1):
                c = total - a - b
                if 0 <= c <= total:
                    result.append((a, b, c))
        return result

    def get_splits_with_permutations(self, total, length):
        result = set()

        def backtrack(path, depth, current_sum):
            if depth == length:
                if current_sum == total:
                    result.update(permutation_set(path))
                return

            for i in range(min(10, total - current_sum + 1)):
                backtrack(path + [i], depth + 1, current_sum + i)

        def permutation_set(arr):
            used = [False] * len(arr)
            perms = set()

            def permute(path):
                if len(path) == len(arr):
                    perms.add(tuple(path))
                    return
                for i in range(len(arr)):
                    if not used[i]:
                        used[i] = True
                        permute(path + [arr[i]])
                        used[i] = False

            permute([])
            return perms

        backtrack([], 0, 0)
        return sorted(result)

    def divideNum(self, n):
        for i in range(n):
            pass

        ele = []
        
        ele.append(n)
        return ele
    
    def process_input(self, data):
        if all(isinstance(x, tuple) for x in data):
            return [''.join(str(i) for i in x) for x in data]

    def digit_sum(self, n):
        return sum(int(d) for d in str(n))

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        digits_low = len(str(low))
        digits_high = len(str(high))
        
        # 2의 제곱인지 확인
        digits = self.makePowerOfTwo(digits_low)
        
		# high보다 자리수가 커지지 않게 start를 계속 2 제곱
        while digits <= digits_high:
            # 해당 자릿수의 경우 찾기
            num_low = 10 ** (digits - 1) + 1
            if num_low < low:
                num_low = low
                
            num_high = 10 ** digits - 1
            if num_high > high:
                num_high = high
                
            # 2의 몇승인가를 기준으로 양옆의 합이 같으면 true
            n = digits.bit_length() - 1
            
            # 앞의 n 자리를 각각 잘라서 가능한 합을 다 구한 후
            possible = list(range(num_low // (10 ** n), (num_high // (10 ** n)) + 1))
            
			# 합의 가능 경우의 수를 다 구한다
            can = []
            for p in possible:
                ele = self.get_splits_with_permutations(self.digit_sum(p), n)
                numbers = self.process_input(ele)
                
                for num in numbers:
                    for num2 in numbers:
                        sample = num + num2
                        if num_low <= int(sample) <= num_high:
                            count+= 1
                        
            digits <<= 1
            
        return count

a = Solution()
print(a.countSymmetricIntegers(1200, 1230))
