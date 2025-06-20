# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        bfs_traverse=[]
        q=deque()
        if root:
            q.append(root)
            bfs_traverse.append(root.val)
        
        while q:
            first=q.popleft()
            # bfs_traverse.append(first.val)
            if first.left:
                bfs_traverse.append(first.left.val)
                q.append(first.left)
            else:
                bfs_traverse.append("null")
            
            if first.right:
                bfs_traverse.append(first.right.val)

                q.append(first.right)
            else:
                bfs_traverse.append("null")
                
        while  bfs_traverse and bfs_traverse[-1]=='null':
            bfs_traverse.pop()      
            
        return " ".join(str(x) for x in bfs_traverse)

            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data=data.split()
        if not data or len(data)==0:
            return None
        
        root=TreeNode(int(data[0]))
        q=deque()
        q.append(root)
        
        n=len(data)
        i=1
        
        while q and i<n:
            node=q.popleft()
            
            #for left child 
            if data[i]!='null':
                node.left=TreeNode(int(data[i]))
                q.append(node.left)
            i+=1
            
            #for right child
            
            if i<n and data[i]!='null':
                node.right=TreeNode(int(data[i]))
                q.append(node.right)
                
            i+=1
            # print(root)
        return root


# বাস্তব জীবনের ব্যবহার (Real-World Applications of Serialize/Deserialize Binary Tree)

# ১. ডাটা ট্রান্সমিশন বা নেটওয়ার্ক কমিউনিকেশন
#    একটি সার্ভার বা ক্লায়েন্টের মধ্যে ট্রি ডাটা পাঠাতে serialize করে string/array বানানো হয়,
#    এবং অপরপ্রান্তে deserialize করে মূল ট্রি reconstruct করা হয়।

# ২. ডাটাবেসে ট্রি স্টোর করা
#    ক্যাটাগরি ট্রি, ফাইল সিস্টেম ট্রি, এক্সপ্রেশন ট্রি ইত্যাদি ডাটাবেসে স্টোর করতে serialize করা হয়।
#    ডাটাবেস থেকে রিড করার সময় deserialize করে পুনরায় ট্রি তৈরি করা হয়।

# ৩. ব্যাকআপ ও রিস্টোর
#    অ্যাপ্লিকেশনের ডেটা বা ট্রি স্ট্রাকচার ব্যাকআপ নিতে serialize করে সংরক্ষণ করা হয়।
#    পরে তা পুনরুদ্ধার (restore) করতে deserialize ব্যবহার হয়।

# ৪. মেশিন লার্নিং (Decision Trees)
#    Decision Tree বা Random Forest মডেল ট্রেন করার পর তা serialize করে সংরক্ষণ করা হয়।
#    এরপর কোনো প্রোডাকশন সিস্টেমে বা অন্য মেশিনে মডেলটি deserialize করে ব্যবহার করা হয়।

# ৫. গেম ডেভেলপমেন্ট (Game State Tree)
#    একটি গেমের সম্ভাব্য সব মুভ বা স্টেট একটি ট্রি-তে থাকে।
#    সেই স্টেট গুলো serialize করে সংরক্ষণ করলে খেলা পুনরায় চালু বা বিশ্লেষণ করা সহজ হয়।

# ৬. কোড পার্সিং ও IDE সাপোর্ট
#    IDE তে পার্সিং এর সময় syntax tree তৈরি হয়। 
#    সেই ট্রি serialize করে রাখা হয় যাতে undo/redo বা static analysis করা যায়।



