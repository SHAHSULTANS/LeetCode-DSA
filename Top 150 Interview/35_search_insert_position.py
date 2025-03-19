from typing import List

from pyparsing import nums

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l,r=0,len(nums)-1
        mid=0
        
        if target>nums[r]:
            return len(nums)
        elif target<nums[0]:
            return 0 
        
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        
        
        
        if nums[mid]>target:
            return mid
        else:
            return mid+1
        # print(mid)




nums=[1,3]
targe=2

ob=Solution()
print(ob.searchInsert(nums,targe))
 
        
        