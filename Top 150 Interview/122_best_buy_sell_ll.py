from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        i=0
        greedy_buy=greedy_sell=0
        while i<n:
            greedy_buy=greedy_sell=prices[i]
            i+=1
            while i<n:
                if greedy_sell<prices[i]:
                    greedy_sell=prices[i]
                elif greedy_buy>prices[i]:
                    profit+=greedy_sell-greedy_buy
                    greedy_sell=greedy_sell=0
                    break
                elif greedy_sell>prices[i]:
                    profit+=greedy_sell-greedy_buy
                    greedy_sell=greedy_sell=0
                    break
                i+=1
           
        return profit+greedy_sell-greedy_buy
                 
                    