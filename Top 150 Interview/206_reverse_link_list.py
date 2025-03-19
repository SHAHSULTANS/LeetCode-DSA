


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        revhead=None
        current=head
        while current:
            next_node=current.next
            current.next=revhead
            revhead=current
            current=next_node
            
        return revhead
        