# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        
        inorder_value_index={value:index for index,value in enumerate(inorder)}
        
        self.postorder_length=len(postorder)-1
        
        def fun(i,j):
            if i>j:
                return None
            
            mid_index=inorder_value_index[postorder[self.postorder_length]]
            self.postorder_length-=1
            
            
            root=TreeNode(inorder[mid_index])
            
            root.right=fun(mid_index+1,j)
            root.left=fun(i,mid_index-1)
            
            return root

        return fun(0,len(inorder)-1)
            
        
        
# 🗂️ 1. ফাইল সিস্টেম পুনর্গঠন (File System Reconstruction)
# কোনো ডিভাইসে ফাইল ও ফোল্ডার গঠন হারিয়ে গেলে, যদি ইন-অর্ডার ও পোস্ট-অর্ডার ট্র্যাভার্সাল সংরক্ষিত থাকে,
# তাহলে মূল ফাইল সিস্টেম স্ট্রাকচার পুনরায় তৈরি করা যায়।

# 📁 2. XML বা JSON Document Tree রিকনস্ট্রাকশন
# অনেক সময় ডেটা ট্রি আকারে থাকে, যেমন XML বা JSON।
# যদি ইন-অর্ডার ও পোস্ট-অর্ডার traversal সংরক্ষিত থাকে, তাহলে ঐ স্ট্রাকচার পুরো reconstruct করা যায়।

# 🧠 3. সিদ্ধান্ত গ্রহণ ট্রি (Decision Tree) রিকনস্ট্রাকশন
# Machine Learning এ decision tree কোনো কারণে নষ্ট হলে বা ট্রেনিং ছাড়াও ইনফারেন্স Tree reconstruct করতে চাইলে,
# ইন-অর্ডার ও পোস্ট-অর্ডার থেকে মূল Tree তৈরি করা যায়।

# 🕵️ 4. Criminal Investigation বা Interrogation Flow Tree পুনর্গঠন
# Law enforcement agency interrogation বা reasoning ট্রি সংরক্ষণের সময় node traversal রেকর্ড করা হয়।
# পরে ঐ traversal থেকে পুরো reasoning স্ট্রাকচার পুনরুদ্ধার করা হয়।

# 💬 5. Chatbot Conversation Tree
# একজন ইউজারের চ্যাট ইতিহাস বা decision path ট্র্যাভার্সাল ফর্মে সংরক্ষিত থাকে।
# ঐ ইন-অর্ডার ও পোস্ট-অর্ডার ডেটা ব্যবহার করে পুরো কনভার্সেশন ফ্লো ট্রি reconstruct করা যায়।

# 🧬 6. Family Tree বা Genealogy Reconstruction
# পূর্বপুরুষদের সম্পর্ক ইন-অর্ডার ও পোস্ট-অর্ডার অনুযায়ী থাকলে,
# ঐ তথ্য ব্যবহার করে পারিবারিক বংশের স্ট্রাকচার বানানো সম্ভব।

# 📊 7. Organizational Hierarchy Tree
# একটি প্রতিষ্ঠানের ম্যানেজমেন্ট স্ট্রাকচার, যেমন CEO থেকে নিচের কর্মচারী পর্যন্ত,
# ইন-অর্ডার ও পোস্ট-অর্ডার ট্রাভার্সালের মাধ্যমে পুনর্গঠন করা যায়।

# 🎮 8. Game AI Decision Trees
# কোনো গেমে প্লেয়ার কীভাবে সিদ্ধান্ত নেয় (AI behavior),
# সেটি ইন-অর্ডার ও পোস্ট-অর্ডার traversal হিসাবে সংরক্ষণ করলে,
# ঐ Tree ব্যবহার করে behavior পুনঃনির্মাণ সম্ভব হয়।

# 📚 9. Compiler Design – Abstract Syntax Tree (AST)
# Compiler ইনপুট কোডকে ট্রি আকারে রূপান্তর করে।
# যদি AST এর ইন-অর্ডার ও পোস্ট-অর্ডার traversal সংরক্ষিত থাকে,
# তাহলে পুরো কোড structure পুনর্গঠন করা সম্ভব।

# 🛰️ 10. Network Packet Tree Reconstruction
# কিছু জটিল নেটওয়ার্ক প্রোটোকলে প্যাকেট ট্রি আকারে সাজানো থাকে (DNS, MIME),
# যেটা ট্রাভার্সাল লজিক অনুযায়ী reconstruct করা যায় ইন-অর্ডার ও পোস্ট-অর্ডার ডেটা থেকে।
    
            
            
            
        
        