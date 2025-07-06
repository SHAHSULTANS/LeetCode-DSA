"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from pyparsing import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # return node
        if node:
            node_map={}
            visited={}
            def dfs_mapping(root):
                # print(root.val)
                node_map[root.val]=Node(root.val)
                visited[root.val]=True
                # print(visited)

                for adjacent in root.neighbors:
                    # print(adjacent," -->",visited.get(adjacent))
                    if visited.get(adjacent.val) is None:
                        
                        dfs_mapping(adjacent)
                        
            dfs_mapping(node)
            # print(node_map)
            q=deque()
            
            visited={}
            q.append(node)
            
            while q:
                font=q.popleft()
                visited[font.val]=True
                if visited.get(font.val) is None:
                    for adjacent in font.neighbours:
                        node_map[font.val].neighbours.append(node_map[adjacent.val])
                        q.append(adjacent)
                
            return node_map(node.val)
                
            
                        
                

        