class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.row=len(grid)
        self.col=len(grid[0])

        def complete_grid(r,c):
            grid[r][c]="0"
            if r-1>=0 and grid[r-1][c]=="1":
                complete_grid(r-1,c)

            if r+1<self.row and grid[r+1][c]=="1":
                complete_grid(r+1,c)

            if c-1>=0 and grid[r][c-1]=="1":
                complete_grid(r,c-1)
            
            if c+1<self.col and grid[r][c+1]=="1":
                complete_grid(r,c+1)


        island=0

        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j]=="1":
                    complete_grid(i,j)
                    island+=1

        return island
        