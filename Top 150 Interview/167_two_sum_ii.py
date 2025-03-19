
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        
        while l<r:
            sum=numbers[l]+numbers[r]
            if(sum==target):
                return [l+1,r+1]
            elif sum>target:
                r-=1
            else:
                l+=1
    
    

numbers = [2,7,11,15,88]
ob=Solution()
print(ob.twoSum(numbers,9))        