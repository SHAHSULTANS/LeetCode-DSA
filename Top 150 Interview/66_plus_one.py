from functools import total_ordering


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=[]
        rem=1
        for item in reversed(digits):
            total_ordering=item+rem
            ans.append(total_ordering%10)
            rem=int(total_ordering/10)
            
        if rem>0:
            ans.append(rem)
        
        return (ans[::-1])