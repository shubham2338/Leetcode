class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        mem={}
        def solve(x,y):
            if x==y: return True
            if len(x)<=1: return False
            n=len(x)
            m=x+y
            if m in mem:
                return mem[m]
            for i in range(1,n):
                if solve(x[:i],y[-i:]) and solve(x[i:],y[:-i]) or solve(x[:i],y[:i]) and solve(x[i:],y[i:]):
                    mem[m]=True
                    return mem[m]
            mem[m]=False
            return mem[m]
        if solve(s1,s2):
            return True
        return False
            
        