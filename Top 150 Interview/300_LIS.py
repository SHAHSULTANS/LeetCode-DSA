
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #But this method or sub[] doesn't contain correct order of LIS. Only give length. Time Complexity O(n*logn)
        sub=[]
        for num in nums:
            index=bisect.bisect_left(sub,num)
            if index==len(sub):
                sub.append(num)
            else:
                sub[index]=num
        
        return len(sub)
        # occurance=[]
        # occurance.append(1)
        
        # for i in range(1,len(nums),1):
        #     occurance.append(1)
        #     for j in range(i):
        #         if nums[i]>nums[j] and occurance[j]+1>occurance[i]:
        #             occurance[i]=occurance[j]+1
                    
        # return max(occurance)