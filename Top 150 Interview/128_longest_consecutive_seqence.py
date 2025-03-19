

from typing import Counter
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap=Counter(nums)
        ans=0
        
        for item in nums:
            dum=item
            while hashmap[dum+1]>0:
                dum+=1
                hashmap.pop(dum)
            
            sum=dum-item
            dum=item
            while hashmap[dum-1]>0:
                dum-=1
                hashmap.pop(dum)
                
            sum+=item-dum+1
            ans=max(ans,sum)
        return ans
            