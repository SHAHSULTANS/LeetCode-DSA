

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ctn=0
        current=head
        while current:
            current=current.next
            ctn+=1
        
        if ctn==1:
            return None
        if n==1:
            current=head
            while ctn-n-1>0:
                current=current.next
                ctn-=1
            current.next=None
            return head
        
        if n==ctn:
            return head.next
        
        current=head
        while ctn-n-1>0:
            current=current.next
            ctn-=1
        current.next=current.next.next
        return head
        
        
        