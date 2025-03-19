
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[]
        prefix.append(nums[0])
        suffix=[]
        suffix.append(nums[n-1])
        for i in range(1,n):
            prefix.append(prefix[i-1]*nums[i])
            suffix.append(nums[n-1-i]*suffix[i-1])
        # print(suffix)
        # print(prefix)
        ans=[]
        ans.append(suffix[n-2])
        for i in range(1,n-1):
            a=prefix[i-1]
            b=suffix[n-2-i]
            ans.append(a*b)
        ans.append(prefix[n-2])
        return ans
        
        
nums = [1,2,3,4]
ob=Solution()
ob.productExceptSelf(nums)
    
    
