


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans=[]
        def fun(root):
            if root is None:
                return
            
            fun(root.left)
            self.ans.append(root.val)
            fun(root.right)
        
        fun(root)
        return all(self.ans[i]<self.ans[i+1] for i in range(len(self.ans)-1))
        # print(self.ans)

  