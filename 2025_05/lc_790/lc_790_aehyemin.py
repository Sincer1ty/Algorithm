class Solution:
    def numTilings(self, n: int) -> int:
        #n=0 => 0
        #n=1 => 1
        #n=2 => 2
        #n=3 => 5
        #n=4 => 11
        #f(n) = 2*f(n-1) + f(n-3)
        dp = [0] * (1000)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        
        for i in range(3,n+1):
            dp[i] =( 2*dp[i-1] + dp[i-3] ) % (10**9 + 7)

        print(dp)
        return dp[n]
