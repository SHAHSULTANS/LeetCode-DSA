# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
        
# from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True

        return False
    
# Linked List Cycle Detection - Real-world Applications (Bangla Examples)

# 1. মেমোরি লিক ডিটেকশন (Memory Leak Detection)
#    - অপারেটিং সিস্টেম বা গার্বেজ কালেকশনে অবজেক্টের মধ্যে সাইক্লিক রেফারেন্স (cyclic reference) 
#      খুঁজে বের করতে ব্যবহৃত হয়।
#    - Example: Python-এর garbage collector cyclic references ডিটেক্ট করে মেমোরি লিক প্রতিরোধ করে।

# 2. ডেটাবেস ডেডলক ডিটেকশন (Database Deadlock Detection)
#    - যখন দুটি ট্রানজেকশন পরস্পরকে লক করে এবং অপেক্ষা করে, তখন ডেডলক হয়।
#    - সাইকেল ডিটেকশন অ্যালগরিদম (যেমন: Wait-for Graph) ব্যবহার করে ডেটাবেস এই সমস্যা সমাধান করে।
#    - Example: PostgreSQL, Oracle-এ Deadlock Detection এর জন্য সাইকেল চেক করা হয়।

# 3. গেম ডেভেলপমেন্ট (Game Development - Enemy AI Pathfinding)
#    - গেমের শত্রুরা যদি প্লেয়ারকে ফোলো করতে গিয়ে একটি লুপে আটকে যায়, 
#      সাইকেল ডিটেকশন অ্যালগরিদম ব্যবহার করে লুপ ডিটেক্ট করা হয়।
#    - Example: PAC-MAN গেমে ভূতের চলার পথে লুপ আছে কিনা তা চেক করা।

# 4. নেটওয়ার্ক রাউটিং লুপ ডিটেকশন (Network Routing Loop Detection)
#    - রাউটিং প্রোটোকল (যেমন: RIP, OSPF) প্যাকেট লস এড়াতে লুপ ডিটেক্ট করে।
#    - Example: কোনো প্যাকেট যদি একই রাউটারে বারবার ঘুরতে থাকে, তাহলে TTL (Time-To-Live) এর মাধ্যমে সাইকেল ডিটেক্ট করা হয়।

# 5. টাস্ক শিডিউলিং (Task Scheduling - Dependency Resolution)
#    - যদি বিভিন্ন টাস্ক একে অপরের উপর নির্ভরশীল হয় এবং সাইকেল তৈরি করে,
#      তাহলে সিস্টেম Hang হতে পারে। সাইকেল ডিটেকশন ব্যবহার করে এটি সমাধান করা হয়।
#    - Example: Makefile-এ টার্গেট ডিপেন্ডেন্সিতে সাইকেল চেক করা।