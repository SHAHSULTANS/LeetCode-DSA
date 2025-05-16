# Problem Statement:
# Given a 2D matrix where each cell has an associated cost for accessing it.
# We need to find the minimum cost to travel from the top-left cell (0, 0)
# to the bottom-right cell (n-1, m-1), where n is the number of rows and m is the number of columns.
# We are only allowed to move to the right or down cell from our current position.
# The goal is to find the path with the minimum total cost.

def minimum_cost(matrix):
    row=len(matrix)
    col=len(matrix[0])
    for i in range(row):
        for j in range(col):
            if i==0 or j==0:
                if i==0 and j>0:
                    matrix[i][j]+=matrix[i][j-1]
                elif j==0 and i>0:
                    matrix[i][j]+=matrix[i-1][j]
            else:
                left_move=matrix[i][j-1]+matrix[i][j]
                down_move=matrix[i-1][j]+matrix[i][j]
                matrix[i][j]=min(left_move,down_move)
                
    return matrix[row-1][col-1]
                
    
matrix = [
    [1, 3, 5],
    [2, 1, 2],
    [4, 3, 1]
]

print(minimum_cost(matrix))  # Output: 7


# -----------------------------------------------------------
# Real-World Applications of Minimum Cost Path (Right/Down) 
# -----------------------------------------------------------

# 1. GPS Navigation / Pathfinding in Maps:
#    - Finding the shortest or least-cost route in a city grid.
#    - Cost may represent distance, time, tolls, or fuel consumption.

# 2. Robot Movement in Factories or Warehouses:
#    - Planning the most efficient path a robot should take.
#    - Cells represent floor tiles with energy or time costs.

# 3. Logistics and Parcel Delivery:
#    - Optimizing delivery routes through a grid of zones or checkpoints.
#    - Useful in courier services, warehouse management, and supply chains.

# 4. Image Processing - Seam Carving:
#    - Finding and removing paths of least importance in an image.
#    - Used for intelligent image resizing without distortion.

# 5. Project Scheduling:
#    - Modeling multi-step tasks in a grid-like structure.
#    - Each task has an associated cost (time, money) to minimize.

# 6. Bioinformatics - Sequence Alignment:
#    - Comparing DNA or protein sequences.
#    - Cost represents mismatch penalties or gap insertions.

# 7. Game Development:
#    - Finding optimal movement in tile-based games or puzzle games.
#    - Can model character movement with energy/terrain penalties.

# 8. Education:
#    - Teaching dynamic programming and optimization strategies.
#    - A foundational problem for learning recursion, memoization, and DP.

# -----------------------------------------------------------
