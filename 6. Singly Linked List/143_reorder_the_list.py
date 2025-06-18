# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            
        middlehead=slow.next
        slow.next=None
        
        # print(head)
        def reverse_middle_list(root):
            if not root or root.next is None:
                return root
            
            revhead=reverse_middle_list(root.next)
            
            root.next.next=root
            root.next=None
            return revhead
        
        reverseMiddleHead=reverse_middle_list(middlehead)
        
        # print(reverseMiddleHead)
        
        copyhead=head
        
        while copyhead and reverseMiddleHead:
            
            a=copyhead.next
            copyhead.next=reverseMiddleHead
            
            b=reverseMiddleHead.next
            reverseMiddleHead.next=a
            
            copyhead=a
            reverseMiddleHead=b
            
            
        