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
    


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hash_map={}
        for powerset_range in range(0,pow(2,len(nums))):
            subset=[]
            for i in range(powerset_range):
                if (powerset_range &(1<<i)):
                    subset.append(nums[i])
                    
            hash_map[tuple(subset)]=1
            
        # return ans
        return [key for key in hash_map]