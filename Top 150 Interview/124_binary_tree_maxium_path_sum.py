# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=root.val

        def dfs(root):
            if not root:
                return 0

            left=max(0,dfs(root.left))
            right=max(0,dfs(root.right))

            current=root.val+left+right
            self.ans=max(self.ans,current)

            return root.val+max(left,right)

            summation+=root.val
            # print(summation)

        dfs(root)
        return self.ans
        