class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        h=s[::-1]
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==h[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
       
        return dp[-1][-1]