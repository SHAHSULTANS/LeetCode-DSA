

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        n=len(nums)
        ans=set()
        for i in range(n-2):
            j,k=i+1,n-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    ans.add((nums[i],nums[j],nums[k]))
                    # print(i," ",j," ",k)
                    k=k-1
                elif sum>0:
                    k-=1
                else:
                    j+=1
        
        res=[list(x) for x in ans]
        return res
            
        
    

nums = [-1,0,1,2,-1,-4]
ob=Solution()
ob.threeSum(nums)