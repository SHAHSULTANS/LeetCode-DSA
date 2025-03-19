
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)-1
        if n==0:
            return 0
        length=n-1
        
        track=[0]*(n+1)
        
        while length>=0:
            # print(nums[length-1])
            # length-=1
            if(nums[length]==0):
                track[length]=100000
                length-=1
                continue
            
            iterate=min(n-length,nums[length])
            
            minvalue=min(track[i] for i in range(length+1,length+iterate+1))+1
            
            track[length]=minvalue       
            
            length-=1

        return track[0]

nums = [10,0,1,1,4,5,6]
ob=Solution()
print(ob.jump(nums))
# print(min([nums[i] for i in range(4)]))