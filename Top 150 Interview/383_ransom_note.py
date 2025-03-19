
from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=Counter(ransomNote)
        m=Counter(magazine)
        
        for char in ransomNote:
            if m[char]<r[char]:
                return False
            
        return True
            