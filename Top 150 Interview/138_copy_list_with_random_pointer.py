"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        random_mapping={}
        
        if head:
            #create new copy head
            newhead=Node(head.val)
            random_mapping[head]=newhead
            
            orginal_head=head
            
            copy_newhead=newhead
            
            #next chainging copy without random
            while orginal_head.next:
                cp=Node(orginal_head.next.val)
                
                #mapping
                random_mapping[orginal_head.next]=cp
                
                copy_newhead.next=cp
                
                orginal_head=orginal_head.next
                copy_newhead=copy_newhead.next
               
            #copy the random
            orginal_head=head
            while orginal_head:
                random_mapping[orginal_head].random=random_mapping.get(orginal_head.random)
                orginal_head=orginal_head.next
            # print(newhead)
            
            return newhead
        
        
        
# -------------------------------------------------------------
# 📚 ১. Versioned Document Cloning (e.g., Google Docs)
# উদাহরণঃ তুমি Google Docs-এ একটি document clone করছো:
# - Paragraph গুলো next pointers দিয়ে যুক্ত
# - কিছু paragraph অন্য paragraph-এর reference (citation) দেয় ➤ random pointers
# - এখন তুমি যখন "Make a copy" ক্লিক করো, তখন পুরা document-এর deep copy দরকার
# - যাতে মূল document এর উপর কোনো পরিবর্তন নতুন কপিকে প্রভাবিত না করে

# -------------------------------------------------------------
# 🧠 ২. Graph-like Linked Data Structure Copy (e.g., Knowledge Graphs)
# উদাহরণঃ Mind-mapping apps বা AI-এর knowledge graph system
# - প্রতিটি topic node ➤ next = পরবর্তী topic
# - random = অন্য context-এর link (related idea)
# - এখন যখন তুমি একটি অংশ clone করো (for subgraph processing), তখন পুরো deep copy দরকার including cross-links

# -------------------------------------------------------------
# 👨‍👩‍👧‍👦 ৩. Social Network Friend Recommendation System
# উদাহরণঃ LinkedIn বা Facebook
# - Each profile = node
# - next = friend suggestion list
# - random = best friend, colleague, or top connection
# - তুমি যখন কোনো user profile-এর একটি কপি তৈরি করো (for analysis), তখন friend links + special relationships সঠিকভাবে map করতে হবে

# -------------------------------------------------------------
# 🧬 ৪. Bioinformatics – Protein Interaction Modeling
# উদাহরণঃ প্রতিটি molecule হচ্ছে একটি node
# - next = linear chain
# - random = cross-molecule bond (e.g., hydrogen bonding)
# - যদি তুমি এই structure simulation এর জন্য copy করতে চাও, তাহলে deep copy দরকার

# -------------------------------------------------------------
# 💡 এই সমস্যাটি ব্যবহার হয় যেখানে:
# - লিংকড স্ট্রাকচার আছে
# - Cross-reference বা context-linking আছে (random pointer)
# - Original structure অপরিবর্তিত রেখে নতুন "independent but identical" version বানাতে হয়

# ✅ তাই এই ধরণের প্রোগ্রাম গুলোতে এই কোড / অ্যালগরিদম অপরিহার্য
# -------------------------------------------------------------
