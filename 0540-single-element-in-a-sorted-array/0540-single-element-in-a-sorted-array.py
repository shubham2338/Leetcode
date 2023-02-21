class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r: 
            mid =(l+r)//2
            if (mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid+1]==nums[mid]):
                l=mid+1
            else:
                r=mid
        return nums[l]
                
            