
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_element=nums[0]
        min_element=min(min_element,nums[len(nums)-1])
        
        #decreasing first
        l,r=0,len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            # print(mid," ",l)
            if l!=mid:
                if nums[mid-1]<nums[mid] and nums[mid]<nums[r]:
                    min_element=min(min_element,nums[mid-1])
                    min_element=min(min_element,nums[mid])
                    r=mid-1
                else:
                    min_element=min(min_element,nums[mid]) 
                    l=mid+1
            else:
                min_element=min(min_element,nums[mid]) 
                l=mid+1
                
                
        l,r=0,len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            
            if r!=mid:
                if nums[mid+1]>nums[mid] and nums[l]<nums[mid]:
                    min_element=min(min_element,nums[mid])
                    l=mid+1
                else:
                    min_element=min(min_element,nums[mid+1])
                    r=mid-1
                    
                    
                # if nums[mid+1]<nums[mid]:
                #     min_element=min(min_element,nums[mid-1])
                #     min_element=min(min_element,nums[mid])
                #     r=mid-1
                # else:
                #     min_element=min(min_element,nums[mid]) 
                #     l=mid+1
            else:
                min_element=min(min_element,nums[mid]) 
                r=mid-1
        
        return min_element