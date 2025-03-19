
from typing import Counter



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        # print(n1," ",n2)
        if n2<n1:
            return False
        
        hmap=Counter(s1)
        hmap2=Counter(s2[:n1])
        
        if hmap==hmap2:
            return True
        
        
        i=0
        for j in range(n1,n2):
            # print(j)
            hmap2[s2[i]]-=1
            hmap2[s2[j]]+=1
            i+=1
            if hmap==hmap2:
                return True
            
        return False