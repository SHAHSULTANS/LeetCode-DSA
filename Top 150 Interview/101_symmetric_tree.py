# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pandas import notnull


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans1,ans2=[],[]
        self.left_subtree(root.left,ans1)
        # print(ans1)
        self.right_subtree(root.right,ans2)
        # print(ans2)
        if ans1!=ans2:
            return False
        else:
            return True

        
    def left_subtree(self,root,ans):
        if root.left is None and root.right is None:
            return
        if root is None:
            ans.append(None)
            return 
        
        self.left_subtree(root.left,ans)
        ans.append(root.val)
        self.left_subtree(root.right,ans)
    
    def right_subtree(self,root,ans):
        if root.left is None and root.right is None:
            return
        if root is None:
            ans.append(None)
            return

        self.left_subtree(root.right,ans)
        ans.append(root.val)
        self.left_subtree(root.left,ans)
        