

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans=[]
        self.preorder(root,ans)
        # print(ans)
        # root=None
        if root:
            # root=None
            root.left=None
            current=root
            for i in range(1,len(ans)):
                current.right=TreeNode(ans[i])

                current=current.right
            current.right=None
    
        # root=(root.right)
        
    def preorder(self,root,ans):
        if root is None:
            return
        
        ans.append(root.val)
        self.preorder(root.left,ans)
        self.preorder(root.right,ans)


    

        