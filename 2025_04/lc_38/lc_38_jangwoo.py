class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = "1" 
        
        for _ in range(2, n + 1):
            parts = []
            cnt = 1 
            
            for i in range(1, len(prev)):
                if prev[i] == prev[i-1]:
                    cnt += 1
                else:
                    parts.append(str(cnt))
                    parts.append(prev[i-1])
                    cnt = 1
                    
            parts.append(str(cnt))
            parts.append(prev[-1])
            prev = "".join(parts)
            
        return prev