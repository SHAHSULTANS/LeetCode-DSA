# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        rt=dummy
        current=head
        while current:
            next_node=current
            ctn=0
            while next_node and current.val==next_node.val:
                ctn+=1
                next_node=next_node.next

            rt.next=current
            rt=rt.next
            current=next_node

        rt.next=None

        return dummy.next





# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         dummy=TreeNode()
#         rt=dummy
        
#         current=head
        
#         while current:
#             ctn=0
#             prev=current
#             while current and head.val==current.val:
#                 prev=current
#                 current=current.next
#                 ctn+=1
            
#             if ctn==1:
#                 rt.next=prev
#                 rt=rt.next
#                 # rt=None

                
#             head=current
            
#         rt.next=None#why rt.next bcs rt contain current unique Node.
#         # print(rt.val)
#         return dummy.next