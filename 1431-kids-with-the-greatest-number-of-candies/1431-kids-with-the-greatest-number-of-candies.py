class Solution:
    def kidsWithCandies(self, c: List[int], ec: int) -> List[bool]:
        ans=[False]*(len(c))
        h=max(c)
        for i in range(len(c)):
            if c[i]+ec>=h:
                ans[i]=True
        return ans