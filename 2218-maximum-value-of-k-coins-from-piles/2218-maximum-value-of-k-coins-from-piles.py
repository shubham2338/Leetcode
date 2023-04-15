class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        for i in range(len(piles)):
            for j in range(1,len(piles[i])):
                piles[i][j]+=piles[i][j-1]
        dp={}
        def fun(piles,i,k):
            if i>=len(piles):
                return 0
            if (i,k) in dp: return dp[(i,k)]
            s=0
            s=max(s,fun(piles,i+1,k))
            for j in range(len(piles[i])):
                if j+1<=k:
                    s=max(s,piles[i][j]+fun(piles,i+1,k-j-1))
                else: break
            dp[(i,k)]=s
            return dp[(i,k)]
        return fun(piles,0,k)