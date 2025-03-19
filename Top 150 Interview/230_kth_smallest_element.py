

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: 
        int) -> int:
        self.ans=None
        self.k=k
        
        def inorder(root):
            if not root or self.ans is not None:
                return
            
            inorder(root.left)
            
            self.k=self.k-1
            
            if self.k==0:
                self.ans=root.val
                return
            
            inorder(root.right)
            
        inorder(root)
        
        return self.ans
                
        
        
        # ans=[]
        # def fun(root,k):
        #     if root is None:
        #         return
        #     fun(root.left,k)
        #     ans.append(root.val)
        #     # if len(ans)==k:
        #     #     return ans[-1]
        #     fun(root.right,k)


        # fun(root,k)
        # return ans[k-1]