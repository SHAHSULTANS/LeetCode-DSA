# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        flag=False
        
        def fun(root,total,targetSum):
            if not root:
                return
            if root.left is None and root.right is None:
                if (total+root.val==targetSum):
                    nonlocal flag
                    flag=True
            fun(root.left,total+root.val,targetSum)
            fun(root.right,total+root.val,targetSum)
            
            
            
        fun(root,0,targetSum)
        return flag