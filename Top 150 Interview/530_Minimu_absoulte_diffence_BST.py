

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def fun(root,ans):
            if root is None:
                return

            fun(root.left,ans)
            ans.append(root.val)
            fun(root.right,ans)
        
        fun(root,ans)
        res=inf
        for i in range(1,len(ans)):
            res=min(res,ans[i]-ans[i-1])
        return res

            
        