from math import inf
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum=0
        ans=(-float('inf'))
        
        for num in nums:
            sum+=num
            # print(sum)
            ans=max(sum,ans)
            ans=max(ans,num)
            if sum<0:
                sum=0


                
        return ans