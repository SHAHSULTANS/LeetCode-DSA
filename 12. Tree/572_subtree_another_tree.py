# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans=False
        
        
        def is_substree(p,q):
            if p is None and q is None:
                return True
            
            if p is None or q is None:
                return False
            
            return (p.val==q.val) and is_substree(p.left,q.left) and is_substree(p.right,q.right)
        
        def dfs(root):
            if root:
                if is_substree(root,subRoot):
                    self.ans=True
                    return
                
                dfs(root.left)
                dfs(root.right)
                

        dfs(root)       
        return self.ans
    
    
    # === Applications of "Subtree of Another Tree" Problem ===

# 1. File System Matching:
#    Checking if a folder structure (e.g., a template folder) exists
#    exactly somewhere inside a larger file system tree.

# 2. Code Plagiarism Detection:
#    Comparing abstract syntax trees (AST) of source codes to detect
#    if a part of one code is structurally copied into another.

# 3. Genome Sequencing:
#    In bioinformatics, identifying whether a specific genetic structure
#    (subtree) exists within a larger DNA or RNA sequence tree.

# 4. DOM Tree Comparison:
#    In web development, detecting whether a certain UI component's
#    DOM structure is reused in other pages or templates.

# 5. Knowledge Graph Pattern Matching:
#    Finding whether a certain relationship structure exists within
#    a bigger semantic or organizational knowledge graph.

# Note: These use cases all involve checking whether a specific tree-shaped
# structure is embedded identically within a larger tree.
