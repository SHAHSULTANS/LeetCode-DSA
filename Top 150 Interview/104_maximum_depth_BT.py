


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from pyparsing import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        ans=-1
        q=deque()
        q.appendleft((root,0))
        
        while q:
            r=q.popleft()
            depth=r[1]
            ans=max(ans,depth+1)
            
            # print(r)
            if r[0].left is not None:
                q.append((r[0].left,r[1]+1))
                ans=max(ans,depth+1)
            if r[0].right is not None:
                q.append((r[0].right,r[1]+1))
                ans=max(ans,depth+1)
                
        return ans