



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans=[]
        
        def fun(root,s):
            if root is None:
                return
            
            
            if s=="":
                s=str(root.val)
            else:
                s+="->"+str(root.val)

            if root.left is None and root.right is None:
                self.ans.append(s)
                
            fun(root.left,s)
            fun(root.right,s)

        fun(root,"")

        return self.ans
    

# 📌 Real-world Applications:

# 1️⃣ File System Traversal:
#    ফাইল সিস্টেম নিজেই একটি Tree (ডিরেক্টরি ও ফাইল সহ) — যেখানে আমরা প্রতিটি ফাইলের সম্পূর্ণ path খুঁজি।
#    উদাহরণ: 
#       C:/User/Documents/file.txt → এটি একটি root-to-leaf path।

# 2️⃣ Decision Tree in Machine Learning:
#    ML এর Decision Tree মডেল এর প্রত্যেকটা leaf node একটা নির্দিষ্ট সিদ্ধান্ত প্রকাশ করে।
#    কোন rule গুলো ফলো করে ঐ সিদ্ধান্তে পৌঁছেছে তা root-to-leaf path ব্যবহার করে পাওয়া যায়।

# 3️⃣ HTML/XML DOM Traversal:
#    HTML বা XML structure একটি Tree — প্রতিটি element node.
#    DOM traversal করে element এর পূর্ণ path বের করা যায় এই root-to-leaf logic দিয়ে।

# 4️⃣ Routing Paths in Networks:
#    Network routing এ বিভিন্ন রাউটিং decision tree তৈরি হয়।
#    প্রতিটি সম্ভাব্য routing path খুঁজে বের করতে Binary Tree Path algorithm ব্যবহার করা যায়।

# 5️⃣ Workflow Systems:
#    একটি Task/Workflow engine যেখানে বিভিন্ন কাজ dependency সহ নির্ধারিত থাকে (as a tree),
#    সেখানে প্রত্যেকটি execution path বের করাও root-to-leaf traversal এর সমান।

# 🎯 Bottom Line:
#    যেকোনো system যেখানে সিদ্ধান্ত, পথ বা প্রসেস ট্রি আকারে সাজানো থাকে,
#    সেখানে Binary Tree Paths algorithm ব্যবহার করে সব সম্ভাব্য উপসংহার বা রাস্তা খুঁজে বের করা যায়।