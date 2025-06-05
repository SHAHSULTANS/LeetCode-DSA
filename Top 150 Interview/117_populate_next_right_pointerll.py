"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from typing import Deque



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # root.next=NULL
        q=Deque()
        if root:
            q.push((0,root))
            
            hmap={}
            while q:
                d=q.popleft()
                level=d[0]
                nod=d[1]
                
                level_left_node=hmap.get(level)
                
                if level_left_node:
                    level_left_node.next=nod
                    
                hmap[level]=nod
                if nod.left:
                    q.append((level+1,nod.left))
                    
                if nod.right:
                    q.append((level+1,nod.right))
                    
                
                
                
                
                
                
        return root