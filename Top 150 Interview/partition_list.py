

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ar1,ar2=[],[]
        
        while head:
            if head.val<x:
                ar1.append(head.val)
            else:
                ar2.append(head.val)
            head=head.next
            
        ar1+=ar2
        dummy=ListNode()
        current=dummy
        for item in ar1:
            current.next=ListNode(item)
            current=current.next
            
        return dummy.next