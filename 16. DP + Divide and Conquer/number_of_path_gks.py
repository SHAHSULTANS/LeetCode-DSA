# Given a grid of size m x n, the task is to determine the number of distinct paths from the top-left corner to the bottom-right corner. At each step, one can either move down or right. Given the integers m and n, return the number of unique paths from the top-left corner to the bottom-right corner.


class Solution:
    def numberOfPaths(self, m, n):
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

            memo[i][j]=recursion(i,j-1)+recursion(i-1,j)
            return memo[i][j]
        
        return recursion(m-1,n-1)
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 or j==0:
        #             memo[i][j]=1
        #         else:
        #             memo[i][j]=memo[i][j-1]+memo[i-1][j]
                    
        # return memo[m-1][n-1]




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        M = int(input())
        N = int(input())

        ob = Solution()
        ans = ob.numberOfPaths(M, N)
        print(ans)

        print("~")

# } Driver Code Ends