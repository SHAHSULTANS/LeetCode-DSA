from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        localmin=prices[0]
        n=len(prices)
        
        for i in range(1,n):
            localmin=min(localmin,prices[i])
            
            if prices[i]>localmin:
                ans=max(ans,prices[i]-localmin)
                
        return ans
        