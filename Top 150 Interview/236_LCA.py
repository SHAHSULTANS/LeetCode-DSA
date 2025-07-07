# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        track_parent={}
        
        def dfs(parent,node,level):
            if not node:
                return
            
            track_parent[node]=(parent,level)
            dfs(node,node.left,level+1)
            dfs(node,node.right,level+1)
            
        
        dfs(None,root,0)
        # print(track_parent)
        
        pa=p
        qa=q
        
        while track_parent[pa][1]>track_parent[qa][1]:
            pa=track_parent[pa][0]
            
        while track_parent[qa][1]>track_parent[pa][1]:
            qa=track_parent[qa][0]
            
            
        while pa!=qa:
            pa=track_parent[pa][0]
            qa=track_parent[qa][0]
        
        return pa
        
            
# 📌 LeetCode 236 - Lowest Common Ancestor (LCA) of a Binary Tree বাস্তব জীবনের ব্যবহার (Real-World Applications in Bangla)
# -----------------------------------------------------------------------------------

# ✅ ১. Family Tree Analysis
# উদাহরণ: Shanto আর Rahim এর পরিবারের মধ্যে সবচেয়ে নিকটতম common ancestor কে?
# Tree = Family Tree
# Node = Person
# LCA = Closest shared ancestor
# ব্যবহার: Genealogy apps, ancestry research

# ✅ ২. Filesystem Directory Navigation
# উদাহরণ: /usr/local/bin/python এবং /usr/local/lib/python3 এর lowest common directory কোনটি?
# Tree = Directory Tree
# Node = File/Folder
# LCA = Common parent folder (/usr/local)
# ব্যবহার: File management tools, IDE path resolution

# ✅ ৩. Ontology / Knowledge Graph Querying
# উদাহরণ: Dog এবং Cat এর common category (Mammal) কী?
# Tree = Taxonomy Tree
# Node = Concept
# LCA = Shared superclass
# ব্যবহার: Semantic search, AI chatbots, NLP applications

# ✅ ৪. Product Categorization in E-commerce
# উদাহরণ: Gaming Laptop এবং Business Laptop এর lowest common category হলো "Laptops"
# Tree = Product Category Tree
# Node = Product Types
# LCA = Shared category
# ব্যবহার: Breadcrumb navigation, category filters, recommendations

# ✅ ৫. Network Routing Optimization
# উদাহরণ: দুটি নোডের মধ্যে common router বা switch কোথায়?
# Tree = Network Topology Tree
# Node = Devices (routers, switches)
# LCA = Closest common router/switch
# ব্যবহার: Network path planning, load balancing

# ✅ ৬. Git Version Control (Finding Merge Base)
# উদাহরণ: দুইটি branch মিশানোর আগে তাদের common commit খুঁজে বের করা
# Tree = Commit History Graph
# Node = Commit
# LCA = Common ancestor commit (merge base)
# ব্যবহার: Git merge, conflict resolution

# ✅ ৭. Game Engine Scene Hierarchy
# উদাহরণ: দুইটি game object এর common parent container খুঁজে বের করা
# Tree = Scene Graph
# Node = Game Object
# LCA = Common container node
# ব্যবহার: UI grouping, physics calculation, rendering optimization

# ✅ ৮. Organizational Chart Management
# উদাহরণ: Shanto আর Tareq এর lowest common manager কে?
# Tree = Organizational Hierarchy Tree
# Node = Employee
# LCA = Common manager
# ব্যবহার: HR systems, approval workflows, team management

# -----------------------------------------------------------------------------------
# 🚨 LCA ব্যবহার না করলে:
# - Slow queries
# - Incorrect relations
# - Merge conflicts বেশি হবে
# - ভুল hierarchy তৈরি হবে
# -----------------------------------------------------------------------------------
# ✅ LCA হচ্ছে একটি গুরুত্বপূর্ণ টুল hierarchical বা tree-structured ডাটার মধ্যে common relationships দ্রুত এবং নির্ভরযোগ্যভাবে বের করতে।
