

from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       
        profit_gas=[]
        for i in range(len(gas)):
            profit_gas.append(gas[i]-cost[i])
            
        ans=sum(profit_gas)
        if(ans>=0):
            ans=0
            res=0
            flag=0
            for index,item in enumerate(profit_gas):
                # print(item, end=" ")
                res=res+item
                if res>=0 and flag==0:
                    # print(index," res: ",res)
                    ans=index
                    flag=1
                elif res<0:
                    res=0
                    flag=0 
            return ans
    
        return -1         
            
        
        
gass = [6,1,4,3,5]
costs = [3,8,2,4,2]
ob=Solution()
print(ob.canCompleteCircuit(gass,costs))