# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        values_index_inorder={value:index for index,value in enumerate(inorder)}
        # print(values_index_inorder)
        self.preindex=0
        
        def fun(i,j):
            if i>j:
                return None
            
            #find the mid index from inorder tree
            mid=values_index_inorder[preorder[self.preindex]]
            # print("i j",i," ",j, " mid ",mid, " preindex ",self.preindex)
            
            root=TreeNode(inorder[mid]) 
            self.preindex+=1
            
            root.left=fun(i,mid-1)
            root.right=fun(mid+1,j)
            
            return root
        
        
        
        
        
        
# 📌 বাস্তব জীবনের ব্যবহার (Real-World Application):

# ধরো, তুমি একটি Web Browser তৈরি করছো বা একটি HTML/XML Parser লিখছো।
# একটি HTML ফাইল হলো এক ধরনের Tree structure (DOM Tree).
# এই Tree গঠনের সময় যদি আমরা DOM-এর Preorder এবং Inorder traversal সংরক্ষণ করি,
# তাহলে সেই ট্রি পুনর্গঠন করা সম্ভব হয়।
# উদাহরণস্বরূপ, একটি HTML নোডের tree structure নিম্নরূপ হতে পারে:

# <body>
#   <div>
#     <p>Hello</p>
#   </div>
#   <span>World</span>
# </body>

# এইটাকে যদি আমরা preorder এবং inorder traversal আকারে সংরক্ষণ করি, 
# তাহলে আমরা পরবর্তীতে XML parser দিয়ে সেই ট্রি reconstruct করতে পারি।

# ✔️ এছাড়াও ব্যবহার হয়:
# 1. Compiler design-এ syntax tree reconstruct করতে
# 2. Database replication বা recovery তে ট্রি structure reconstruct করতে
# 3. Game development-এ behavior tree বা scene graph reconstruct করতে
# 4. Network protocol analyzer-এ packet dependency tree reconstruct করতে

# ✅ এই কারণে preorder এবং inorder সংরক্ষণ করাটা অনেক গুরুত্বপূর্ণ — কারণ pointer বা memory reference 
# আমরা disk-এ সংরক্ষণ করতে পারি না, কিন্তু traversal list সংরক্ষণ করে গঠন পুনরুদ্ধার করতে পারি।
