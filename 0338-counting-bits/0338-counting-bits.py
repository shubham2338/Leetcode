class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for i in range(n+1):
            x=bin(i)
            h=x.count('1')
            ans[i]=h
        print(ans)
        return ans