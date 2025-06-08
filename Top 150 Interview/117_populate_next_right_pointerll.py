"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""




class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def get_cousin_node(node):
            while node:
                if node.left:
                    return node.left
                
                if node.right:
                    return node.right
                
                node=node.next
            
            return None
        
        def fun(root):
            if not root:
                return 
            
            if root.left:
                root.left.next=root.right
            
            if root.next:
                cousin_connect=get_cousin_node(root.next)
                if cousin_connect:
                    if root.right:
                        root.right.next=cousin_connect
                    elif root.left:
                        root.left.next=cousin_connect
            
            
            fun(root.right) #At first we traverse right subtree because chain are made of form L->R
            fun(root.left)
         
        fun(root)    
        return root
        
            
            # q.push((0,root))
            
            # hmap={}
            # while q:
            #     d=q.popleft()
            #     level=d[0]
            #     nod=d[1]
                
            #     level_left_node=hmap.get(level)
                
            #     if level_left_node:
            #         level_left_node.next=nod
                    
            #     hmap[level]=nod
            #     if nod.left:
            #         q.append((level+1,nod.left))
                    
            #     if nod.right:
            #         q.append((level+1,nod.right))
                    
        
        
                
# ✅ Real-World Application of "Populating Next Right Pointers in Each Node II"

# 🔸1. DOM Tree Rendering (Web Browsers):
# যখন কোনো ব্রাউজার একটি HTML বা XML ডকুমেন্টকে DOM Tree-তে রূপান্তর করে,
# তখন প্রতিটি node এর "next sibling" কে খুঁজে বের করতে হয়।
# এই সমস্যাটি ঠিক সেরকম — প্রতিটি DOM node-এর পরবর্তী ভাই কে সেট করা।

# 🔸2. UI Widget Trees (Mobile/Desktop apps):
# UI rendering systems-এ একাধিক UI components (widgets) একটি tree-তে থাকে।
# Traversal বা rendering optimization-এর জন্য প্রতিটি component-এর next widget কে যুক্ত রাখা গেলে 
# rendering দ্রুত হয়।

# 🔸3. Network Routing Trees:
# ডেটা প্যাকেট ফ্লো করার সময় network structure কখনও tree-র মতো হয়।
# তখন প্রতিটি node (router/switch)-এর "next connected node in same level" জানলে 
# দ্রুত প্যাকেট পাঠানো যায়।

# 🔸4. File System Directory Visualization:
# কোনো ডিরেক্টরির ভেতরের structure কে visualize বা process করতে গিয়ে 
# একটি tree structure তৈরি হয়। সেখানে প্রতিটি ফোল্ডারের "same-level next" জানলে 
# traversal efficient হয়।

# 🔸5. Multiplayer Game Trees:
# কিছু multiplayer games (যেমন strategy games) internal state tracking এর জন্য tree structure ব্যবহার করে।
# একই লেভেলের সকল player বা move এর "next" জানতে হলে এই ধরনের pointer দরকার হয়।

# 🔸6. Memory Optimization in Custom Trees:
# যখন নিজের কোনো custom tree বানিয়ে traversal করতে হয় (যেমন: expression trees, AI decision trees),
# তখন `next` pointers যোগ করে BFS traversal না করেও লেভেল ধরে এগোনো যায় — যা সময় বাঁচায়।

# 🧠 Bottom Line:
# এটি এমন সব জায়গায় দরকার যেখানে:
# - একটি tree structure আছে
# - এবং "same-level next node" quickly খুঁজে বের করার প্রয়োজন
# - BFS traversal costly বা অতিরিক্ত মেমোরি খরচ সাশ্রয় করতে চাই
                
                
                
                
                