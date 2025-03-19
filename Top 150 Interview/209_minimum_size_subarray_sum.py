

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        precompute=[]
        res=0
        for item in nums:
            res+=item
            precompute.append(res)

        index=0
        minsize=1000000
        for i,item in enumerate(precompute):
            if item>=target:
                minsize=min(minsize,i+1)
                while item-precompute[index]>=target and index<i:
                    minsize=min(minsize,i-index)
                    index+=1
        
        if minsize==1000000:
            return 0
        else:
            return minsize