# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count=0

        def dfs(root,maximum):
            if not root:
                return
            
            if root.val>=maximum:
                self.count+=1
            if root.left:
                dfs(root.left,max(maximum,root.val))
            if root.right:
                dfs(root.right,max(maximum,root.val))   

        dfs(root,root.val)

        return self.count