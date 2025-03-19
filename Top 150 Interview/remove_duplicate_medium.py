from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        ctn=1
        index=-1
        k=0
        while i<len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j+=1
                ctn+=1
                # print(ctn)
                
            if ctn>=2:
                k+=2
                index+=1
                nums[index]=nums[i]
                index+=1
                nums[index]=nums[i]
            else:
                k+=1
                index+=1
                nums[index]=nums[i]
            # print(i," ",j," ",ctn)
            
            i=j
            ctn=1
            j=j+1
            
        return k
                
        # while i<len(nums):
        #     # print(nums)
            
        #     while (nums[j]==duplict) and (j<len(nums)):
        #         j+=1
        #         ctn+=1
        #         if(j==len(nums)):
        #             # print(j)
        #             break
        #     if ctn>=2:  
        #         # print(ctn)
        #         k+=2
        #         updateindex+=1
        #         nums[updateindex]=duplict
        #         updateindex+=1
        #         nums[updateindex]=duplict
        #     else:
        #         k+=1
        #         updateindex+=1
        #         nums[updateindex]=duplict
        #     if(j<len(nums)):
        #         duplict=nums[j]
        #     print(i," ",j," ",k," ",ctn," ")
        #     i+=ctn 
        #     j=i
        #     ctn=1
         
        
        
        
#TODO: 


#TODO:(income)
nums = [1, 1, 1, 2, 2, 3]
ob=Solution()
ob.removeDuplicates(nums)
print(nums)