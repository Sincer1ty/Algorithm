# class Solution:
#     def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
#         result = []
        
#         digits_len = len(digits)
        
#         for i in range(digits_len):
#             for j in range(digits_len):
#                 if i == j:
#                     continue
#                 for k in range(digits_len):
#                     if i == k or j == k:
#                         continue
#                     first_digit = digits[i]
#                     second_digit = digits[j]
#                     third_digits = digits[k]
                    
#                     if first_digit == 0:
#                         continue
#                     if third_digits % 2 != 0:
#                         continue
                    
#                     number = first_digit * 100 + second_digit * 10 + third_digits * 1
                    
#                     if number not in result:
#                         result.append(number)
        
#         return sorted(result)
# time limit
# -----------------------------------------------------------------------------------------------------------------

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        result = set()
        
        digits_len = len(digits)
        
        for i in range(digits_len):
            for j in range(digits_len):
                if i == j:
                    continue
                for k in range(digits_len):
                    if i == k or j == k:
                        continue
                    
                    first_digit = digits[i]
                    second_digit = digits[j]
                    third_digits = digits[k]
                    
                    if first_digit == 0:
                        continue
                    if third_digits % 2 != 0:
                        continue
                    
                    number = first_digit * 100 + second_digit * 10 + third_digits * 1
                    
                    if number not in result:
                        result.add(number)
        
        return sorted(result)