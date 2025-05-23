# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listdata=[]
        current=head
        while current:
            listdata.append(current.val)
            current=current.next
        
        i,j=0,len(listdata)-1
        
        while i<j:
            if listdata[i] != listdata[j]:
                return False

            i+=1
            j-=1

        return  True

        