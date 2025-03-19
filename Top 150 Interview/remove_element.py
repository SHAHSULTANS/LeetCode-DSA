from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=j=0
        for i in range(len(nums)):
            if(nums[i]!=val):
                print(nums[i]," ",val)
                nums[j]=nums[i]
                j+=1
                
        return j+1
                
                
    
nums =[3,2,2,3]

ob=Solution()

ob.removeElement(nums, 3)
print(nums)
    
    
    
    