

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n=len(nums)
        root_postion=n//2
        root=TreeNode(nums[root_postion])
        
        current=root.left
        ctn=root_postion-1
        while ctn>=0:
            current=TreeNode(nums[ctn])
            current=current.left
            ctn-=1
            
        ctn=root_postion+1
        current=root.right
        
        while ctn<n:
            current=TreeNode(nums[ctn])
            current=current.right
            ctn+=1
            
        return root
            
        
        
        
        