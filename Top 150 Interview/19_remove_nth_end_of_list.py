# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        slow=fast=dummy
        
        while(n+1>0):
            fast=fast.next
            n=n-1
            
        while fast:
            fast=fast.next
            slow=slow.next
            
        slow.next=slow.next.next
        
        return dummy.next
        
        
        
        
# 📁 1. ফাইল বা ডেটা ব্যাকআপ থেকে পুরনো আইটেম মুছে ফেলা
# অনেক ব্যাকআপ সিস্টেমে সর্বশেষ Nটি ব্যাকআপ রাখা হয়।
# যখন নতুন ব্যাকআপ যোগ করা হয়, তখন N-তম পুরনো ব্যাকআপ (end থেকে) ডিলিট করতে হয়।

# 📧 2. Email inbox বা chat app-এ পুরনো মেসেজ auto-delete করা
# যদি ইউজার বলে “শেষ 10টা ছাড়া বাকি সব মুছে ফেলো”, তাহলে ঐ লজিক প্রয়োগ করে
# N-তম মেসেজ from end খুঁজে, সেখান থেকে সব মেসেজ মুছে ফেলা হয়।

# 🏃 3. Task management system-এ নির্দিষ্ট পুরনো কাজ বাদ দেওয়া
# ধরো ইউজারের task list এ শেষ থেকে 3 নম্বর কাজটি ভুল ছিল — তখন exact Nth task from end খুঁজে remove করা হয়।

# 🎞️ 4. Video streaming queue থেকে শেষের দিকের নির্দিষ্ট ভিডিও বাদ দেওয়া
# ইউজার হয়তো বলে: “শেষ থেকে দ্বিতীয় ভিডিওটা সরিয়ে দাও” — ওই অবস্থায় এই লজিক ব্যবহার করা হয়।

# 📦 5. Order history বা transaction list থেকে নির্দিষ্ট পুরনো item বাদ দেওয়া
# কোনো ইউজার যদি বলে, “আমার শেষ থেকে পঞ্চম অর্ডার বাতিল করো”, তখন সে order list থেকে removeNthFromEnd প্রয়োগ করা হয়।

# 📊 6. Stock price বা sensor data series থেকে নির্দিষ্ট পুরনো entry সরানো
# Continuous data stream থেকে কিছু নির্দিষ্ট দুরত্বের পুরনো তথ্য (N-th from end) remove করে ফেলা হয়,
# যেন memory বা analytics system overloaded না হয়।

# 📚 7. Browsing history থেকে শেষ দিকের নির্দিষ্ট URL মুছে ফেলা
# ধরো তুমি কোনো browser extension বানাচ্ছো, যেখানে ইউজার request করে:
# “শেষ থেকে দ্বিতীয় visited site মুছে দাও” — তখন ওই লজিক দিয়ে exact node delete করা হয়।

# 📝 8. Undo History Stack থেকে নির্দিষ্ট পুরনো action বাদ দেওয়া
# কিছু system এ পুরনো undo/redo action ইতিহাস ম্যানেজ করতে হয় — তখন N-th action from end delete করতে হয়।
