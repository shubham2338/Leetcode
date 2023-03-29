class Solution(object):
    def maxSatisfaction(self, sat):
        mem={}
        def fun(arr,i,t):
            if i==len(arr):
                return 0
            if (i,t) in mem:
                return mem[(i,t)]
            ic=arr[i]*(t+1)+fun(arr,i+1,t+1)
            ex=0+fun(arr,i+1,t)
            mem[(i,t)]=max(ic,ex)
            return max(ex,ic)
        
        sat.sort()
        return fun(sat,0,0)
        
        
        
        