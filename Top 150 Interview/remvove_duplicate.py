from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #Convensional Way
        
        # copyar=[]
        # for item in nums:
        #     if item not in copyar:
        #         copyar.append(item)
                
        # nums[:]=copyar
        # print(nums)
        # return len(nums)
        

        # Efficient Way.
        i=0
        j=1
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
                
        return i+1
    
    
    
    
        
nums=[1, 3, 5, 8, 5]

ob=Solution()
ob.removeDuplicates(nums)


cpy=nums
print(id(cpy))
print(id(nums))

