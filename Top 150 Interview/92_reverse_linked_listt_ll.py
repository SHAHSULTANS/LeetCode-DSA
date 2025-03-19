
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        list_value=[]
        while head:
            list_value.append(head.val)
            head=head.next
        
        rv=list_value[left-1:right]
        rv.reverse()
        list_value[left-1:right+1]=rv
        # print(rv)
        dummy=TreeNode()
        current=dummy
        for item in list_value:
            print(dummy)
            current.next=TreeNode(item)
            current=current.next
            
        return dummy.next