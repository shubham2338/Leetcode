class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=0
        i=0
        j=len(nums)-1
        m=10**9+7
        while i<=j:
            if nums[i]+nums[j]>target:
                j-=1
            else:
                res+=pow(2,j-i,m)
                i+=1
        return res%m