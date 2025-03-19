from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)-1
        if(n==0):
            return True
        n=n-1
        answer=True
        while n>=0:
            if(nums[n]==0):
                answer=False
                ctn=0
                while n>=0:
                    # print(ctn," ",nums[n])
                    if(ctn<nums[n]):
                        answer=True
                        break
                    else: 
                        n=n-1
                    ctn+=1
               
            n-=1
        return answer
    
    
nums = [3,0,1,0,0]
ob=Solution()
print(ob.canJump(nums))