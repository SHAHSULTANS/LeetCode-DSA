class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        
        pathcount=[[0]*col for _ in range(row)]
        # print(pathcount)
        
        #For first row, range up to col
        for i in range(col):
            if obstacleGrid[0][i]==0:
                pathcount[0][i]=1
            else:
                break
            
        #For first column, range up to row
        for j in range(row):
            if obstacleGrid[j][0]==0:
                pathcount[j][0]=1
            else:
                break
            
        for i in range(2,row):
            for j in range(2,col):
                if obstacleGrid[i][j]==0:
                    pathcount[i][j]=pathcount[i-1][j]+pathcount[i][j-1]
                    
        return pathcount[row-1][col-1]
    

# Problem: 63. Unique Paths II (Leetcode)
# Real-world Applications:

# 1. Robot Navigation in Factories:
#    Robots moving in grid-like factory floors with obstacles (e.g., machinery).
#    This algorithm helps calculate how many possible ways a robot can reach its goal.

# 2. Path Planning in Warehouses:
#    In logistics (e.g., Amazon warehouses), robots or workers need to find
#    alternate paths avoiding blocked aisles to reach products.

# 3. Game Development:
#    NPCs (non-player characters) or characters navigating game maps with blocked paths.
#    AI uses this approach to calculate accessible paths.

# 4. Traffic and Logistics Routing:
#    Calculating valid delivery or transportation paths when certain roads are blocked 
#    (due to construction, accidents, etc.).

# 5. Medical Robots in Hospitals:
#    Automated delivery robots (e.g., in smart hospitals) calculating safe paths 
#    to deliver medicines avoiding quarantined or restricted areas.
