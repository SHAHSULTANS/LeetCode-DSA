

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        q=deque()
        if root:
            q.append((root,1))
            
        while q:
            qleft=q.popleft()
            l=qleft[1]
            node=qleft[0]
            
            while(len(ans)<l):
                ans.append([])
                
            ans[l-1].append(node.val)
            
            if node.left:
                q.append((node.left,l+1))
             
            if node.right:
                q.append((node.right,l+1) )
                
        for i in range(1,len(ans),2):
            ans[i].reverse()
        
        return ans      