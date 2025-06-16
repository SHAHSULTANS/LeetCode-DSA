class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(candidates)
        
        def dfs(ar,index,summation):
            if summation>target:
                return
            if summation==target:
                ans.append(ar.copy())
                return
                
            
            for i in range(index,n,1):
                ar.append(candidates[i])
                summation=summation+candidates[i]
                dfs(ar,i,summation)
                ar.pop()
                summation=summation-candidates[i]
            return
        
        dfs([],0,0)
        return ans