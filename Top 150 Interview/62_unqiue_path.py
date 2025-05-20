class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo=[[-1]*n for _ in range(m)]
        # print(memo[0][0])
        # total=0
        
        def recursion(i,j):
            if memo[i][j]!=-1:
                return memo[i][j]
            
            if i<0 or j<0:
                return 0
            if i==0 or j==0:
                memo[i][j]=1
                return memo[i][j]

            memo[i][j]=(recursion(i,j-1)+recursion(i-1,j))
            return memo[i][j]