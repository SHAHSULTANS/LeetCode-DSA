
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        
        #At first check first index means 0.zero based index
        if(n==1) or nums[0]>nums[1]:
            return 0
        
        #Then Check last index means (n-1).zero based index
        if nums[n-1]>nums[n-2]:
            return n-1
        
        l,h=0,n-1
        
        while l<=h:
            mid=int((l+h)/2)
            
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            
            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                h=mid-1
        
        