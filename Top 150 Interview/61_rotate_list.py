

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from pyparsing import deque


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ctn=0
        current=head
        ans=[]
        
        while current:
            # last=current
            ans.append(current.val)
            current=current.next
            ctn+=1
        
        last=None
        # print(head)    
        if ctn==0:
            return head
        
        dq=deque(ans)
        dq.rotate(k%ctn)
        # print(dq)
        dummy=ListNode()
        current=dummy
        for item in dq:
            current.next=ListNode(item)
            current=current.next
        return dummy.next
            