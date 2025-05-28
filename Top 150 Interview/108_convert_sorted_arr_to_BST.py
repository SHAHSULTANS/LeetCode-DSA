# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def fun(start,end,nums):
            if start>end:
                return None
            
            mid=(start+end)//2

            root=TreeNode(nums[mid])
            root.left=fun(start,mid-1,nums)
            root.right=fun(mid+1,end,nums)
            return root
        return fun(0,len(nums)-1,nums)
