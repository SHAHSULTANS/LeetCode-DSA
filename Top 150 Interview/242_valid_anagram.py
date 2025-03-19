
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=Counter(s)
        t=Counter(t)
        return s==t
        # print(s," ",t)
        # s=sorted(s)
        # t=sorted(t)
        # return s==t
   
   
s ="anagram"
t = "nagaram"
ob=Solution()
print(ob.isAnagram(s,t))