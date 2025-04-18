from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        map=Counter(s)
        self.odd=False
        self.total=0
        for key in map:
            if map[key]%2==0:
                self.total+=map[key]
            else:
                self.odd=True
                self.total+=(map[key]-1)

        return self.total if self.odd==False else self.total+1

        