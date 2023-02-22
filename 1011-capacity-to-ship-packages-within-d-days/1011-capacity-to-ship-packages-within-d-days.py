class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def fun(m,days):
            d=1
            t=0
            for w in weights:
                t+=w
                if t>m:
                    t=w
                    d+=1
                    if d>days:
                        return False
            return True
                    
        i,j=max(weights),sum(weights)
        while i<j:
            m=(i+j)//2
            if fun(m,days):
                j=m
            else:
                i=m+1
        return i
                