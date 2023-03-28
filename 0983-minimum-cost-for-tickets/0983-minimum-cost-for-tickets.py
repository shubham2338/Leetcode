class Solution(object):
    def mincostTickets(self, days, costs):
        mem={}
        def fun(d,c,i):
            if i>=len(d):
                return 0
            if i in mem:
                return mem[i]
            a0=c[0]+fun(d,c,i+1)
            j=i
            while j<len(d) and d[j]<d[i]+7:
                j+=1
            
            a1=c[1]+fun(d,c,j)
            j=i
            while j<len(d) and d[j]<d[i]+30:
                j+=1
          
            a2=c[2]+fun(d,c,j)
            
            mem[i]=min(a0,min(a1,a2))
            return mem[i]

        h=fun(days,costs,0)
        return h

        