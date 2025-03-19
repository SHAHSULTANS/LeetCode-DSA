

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        def fun(root,sum_st=0):
            print(sum_st)
            if root is None:
                return sum_st
            # if root.left:
            return fun(root.left,sum_st*10+root.val)+fun(root.right,sum_st*10+root.val)

        return fun(root,0)
        # return ans
        # ans="0"+"5"+"6"+"5"
        # print(int(ans))