
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        occurance=[]
        occurance.append(1)
        
        for i in range(1,len(nums),1):
            occurance.append(1)
            for j in range(i):
                if nums[i]>nums[j] and occurance[j]+1>occurance[i]:
                    occurance[i]=occurance[j]+1
                    
        return max(occurance)