class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r=len(board)
        c=len(board[0])
        def dfs(i,j):
            if i>=r or j>=c or i<0 or j<0:
                return
            
            if board[i][j]=='O':
                board[i][j]='a'
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        #for first row and last row. so iterate to col
        for i in range(len(board[0])):
            if board[0][i]=='O':
                dfs(0,i)
            if board[r-1][i]=='O':
                dfs(r-1,i)

        for j in range(len(board)):
            if board[j][0]=='O':
                dfs(j,0)
            if board[j][c-1]=='O':
                dfs(j,c-1)

        for i in range(r):
            for j in range(c):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='a':
                    board[i][j]='O'
        # print(board)



# ============================================
# 🧠 Real-World Applications of Surrounded Regions Problem
# (Like Leetcode 130)
# ============================================

# 1. 🖼️ Image Segmentation / Region Filling
#    - Use-case: In photo editing tools like Photoshop.
#    - When a user clicks to fill a region with color,
#      we need to detect if the region is enclosed (surrounded by borders).
#    - Similar to how we convert surrounded 'O's to 'X's in the problem.

# 2. 🎨 Flood Fill Algorithm (Paint Bucket Tool)
#    - Use-case: Microsoft Paint and other drawing apps.
#    - When you click to fill a color, the program checks how far
#      it can spread based on boundaries — like detecting surrounded areas.

# 3. 🎮 Game Design – Territory Capture (e.g., Go, Othello)
#    - Use-case: In board or strategy games.
#    - When you surround the opponent's pieces, those areas are captured.
#    - Similar to replacing surrounded 'O's with 'X's.

# 4. 🔥 Forest Fire Simulation
#    - Use-case: Modeling fire spread in a forest.
#    - Enclosed regions (not connected to the edge/wind/water) may burn completely.
#    - Helps determine which areas are "surrounded" by fire-prone zones.

# 5. 🧠 Medical Imaging (Tumor or Region Detection)
#    - Use-case: MRI/CT scans analyzing tissue regions.
#    - Detecting regions fully surrounded by other tissue types.
#    - Like finding 'O's fully surrounded by 'X's.

# ============================================
# 📝 Summary:
# - Core idea: Identify regions that are fully enclosed/surrounded.
# - The DFS/BFS used in this problem is very useful in:
#     * Graphics
#     * Games
#     * Simulation
#     * Image processing
#     * Medical analysis
# ============================================
