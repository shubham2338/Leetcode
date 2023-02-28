class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s=set()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                d={}
                for k in range(j+1,len(nums)):
                    var=-(nums[i]+nums[j]+nums[k])+target
                    if var in d:
                        l=[nums[i],nums[j],nums[k],var]
                        l.sort()
                        s.add(tuple(l))
                    d[nums[k]]=1
        return s
                    
