class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hash_map={}
        subset_ar=[]
        def dfs(i):
            if i>=len(nums):
                hash_map[tuple(subset_ar.copy())]=1
                return

            subset_ar.append(nums[i])
            dfs(i+1)

            subset_ar.pop()
            dfs(i+1)

        dfs(0)
        return [key for key in hash_map]