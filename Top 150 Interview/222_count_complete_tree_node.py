

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l=r=0
        currrent=root
        while currrent:
            currrent=currrent.left
            l+=1
        
        currrent=root
        while currrent:
            currrent=currrent.right
            r+=1
        
        if l==r:
            return (2**l)-1
        
        return 1+ self.countNodes(root.left)+self.countNodes(root.right)
        
    # def count_node(self,root):
    #     if root is None:
    #         return 0
        
    #     return 1+self.count_node(root.left)+self.count_node(root.right)
        
        
    
    