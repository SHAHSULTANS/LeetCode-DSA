

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pyparsing import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        q=deque()
        q.append((root,0))
        # print(q)
        while q:
            top=q.popleft()
            while len(ans)<top[1]+1:
                ans.append([])
            ans[top[1]].append(top[0].val)
            
            if top[0].left:
                q.append((top[0].left,top[1]+1))
                
            if top[0].right:
                q.append((top[0].right,top[1]+1))
        
        return ans
        