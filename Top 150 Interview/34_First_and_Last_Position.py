from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)-1
        
        l,r=0,n
        # print(l," ",r)
        
        leftindex=-1
        while l<=r:
            mid=int((l+r)/2)
            # print(l," ",r)
            if nums[mid]==target:
                leftindex=mid
                r=mid-1
            else:
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
                    
        
        rightindex=-1
        l,r=0,n
        while l<=r:
            mid=int((l+r)/2)
            # print(l," ",r)
            if nums[mid]==target:
                rightindex=mid
                l=mid+1
            else:
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
                    
        if leftindex>=0 and rightindex>=0:
            return[leftindex,rightindex]
        elif leftindex>=0 or rightindex>=0:
            leftindex=max(leftindex,rightindex)
            return[leftindex,rightindex]
        else:
            return [-1,-1]
                    
            
        
        
        
nums = [5,7,7,8,8,10] 
target = 8
ob=Solution()
ob.searchRange(nums,target)