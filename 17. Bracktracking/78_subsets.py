class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        subset_ar=[]
        def dfs(i):
            if i>=len(nums):
                ans.append(subset_ar.copy())
                return

            subset_ar.append(nums[i])
            dfs(i+1)

            subset_ar.pop()
            dfs(i+1)

        dfs(0)
        return ans
    
    
    
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        for powerset_range in range(0,pow(2,len(nums))):
            subset=[]
            for i in range(powerset_range):
                if (powerset_range &(1<<i)):
                    subset.append(nums[i])
                    
            ans.append(subset)
            
        return ans

                