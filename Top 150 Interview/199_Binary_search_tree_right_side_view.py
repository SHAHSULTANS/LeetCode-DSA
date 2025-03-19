

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pyparsing import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        ans={}
        if root:
            q.append((root,0))
        
        while q:
            qleft=q.popleft()
            level=qleft[1]
            root=qleft[0]
            ans[level+1]=root.val
            # print(root.val)
            
            if root.left:
                q.append((root.left,level+1))
                
            if root.right:
                q.append((root.right,level+1))
                
        return [ans[i+1] for i in range(len(ans))]       