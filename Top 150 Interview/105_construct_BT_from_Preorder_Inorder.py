# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        
        inorder_root_index=inorder.index(preorder[0])
        compare_index=inorder_root_index
        
        current=root=TreeNode(preorder[0])
        
        for i in range(1,inorder_root_index+1):
            index_value=inorder.index(preorder[i])
            if index_value<compare_index:
                current.left=TreeNode(preorder[i])
                current=current.left
            elif index_value>compare_index:
                current.right=TreeNode(preorder[i])
                current=current.right
            compare_index=index_value
            
        current=root
        compare_index=inorder_root_index
        
        for i in range(inorder_root_index+1,len(preorder)):
            index_value=inorder.index(preorder[i])
            if index_value<compare_index:
                if current.left is None:
                    current=current.left
                current=TreeNode(preorder[i])
                # current=current.left
            elif index_value>compare_index:
                if current.right is None:
                    current=current.right
                current.right=TreeNode(preorder[i])
                # current=current.right
            compare_index=index_value
            
        return root
            
        
                
        
        