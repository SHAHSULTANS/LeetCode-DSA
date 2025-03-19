# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans=[]
        rem=0
        temp=l1
        while True:
            sum=rem
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            ans.append(sum%10)
            rem=sum//10
            if l1 is None and l2 is None:
                if rem>0:
                    ans.append(rem)
                break
        
        dummy=ListNode()
        current=dummy
        for  value in ans:
            current.next=ListNode(value)
            current=current.next
        
        return dummy.next
        # print(ans)