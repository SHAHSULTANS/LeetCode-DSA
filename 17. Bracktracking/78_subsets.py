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

                