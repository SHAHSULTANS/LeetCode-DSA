class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        j=len(s)
        memo=[[-1]*j for _ in range(j)]
        
        def dp(i,j):
            if memo[i][j]!=-1:
                return memo[i][j]
            if i==j:
                return 1
            if i>j:
                return 0
            
            if s[i]==s[j]:
                memo[i][j]= 2+ dp(i+1,j-1)
                return memo[i][j]
            else:
                memo[i][j]= max(dp(i+1,j),dp(i,j-1))
                return memo[i][j]

        return dp(0,j-1)