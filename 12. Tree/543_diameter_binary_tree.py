# Applications of Binary Tree Diameter Problem:
#
# 1. Compiler Design:
#    - Abstract Syntax Tree (AST) এর মধ্যে সবচেয়ে দীর্ঘ nested expression chain বের করা।
#    - Example: (((a+b) * c) - d) / e → diameter বোঝাবে কত গভীর nesting আছে।
#
# 2. Task Scheduling / Dependency Resolution:
#    - Longest dependency chain বের করতে।
#    - Example: Task A → Task B → Task C → Task D (diameter = 4 tasks)।
#
# 3. Decision Trees (Machine Learning):
#    - Classify করার জন্য worst-case কতগুলো decision নিতে হবে সেটা নির্ণয়।
#    - Example: কোনো animal কে identify করতে সবচেয়ে দীর্ঘ প্রশ্নমালা।
#
# 4. Computer Networks:
#    - Network tree topology তে longest communication path = worst-case latency।
#    - Example: Server A ↔ B ↔ C ↔ D → diameter = 3 hops।
#
# 5. File Systems:
#    - Directory tree তে সবচেয়ে দীর্ঘ ফাইল-টু-ফাইল path বের করা।
#    - Example: /root/folder1/sub1/sub2/fileA → /root/folder2/subx/fileB
#
# 6. Evolutionary Biology (Phylogenetic Trees):
#    - সবচেয়ে দূরের দুই প্রজাতির evolutionary distance নির্ণয় করা।
#    - Example: Fish → Amphibian → Reptile → Mammal → Human (diameter = 5)।

# -----------------------------------------------------------
# কোড: Diameter of Binary Tree বের করা
# -----------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs2(node):
            if not node:
                return 0
            left = 1 + dfs2(node.left)
            right = 1 + dfs2(node.right)
            self.ans = max(self.ans, (left + right))
            return max(left, right)
        
        dfs2(root)
        return self.ans - 2
