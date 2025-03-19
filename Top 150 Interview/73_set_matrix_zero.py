class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        c=len(matrix[0])
        r=len(matrix)
        
        affect_row=set()
        affect_col=set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    affect_row.add(i)
                    affect_col.add(j)
                    
        #set row zeros
        for rownumber in affect_row:
            for j in range(c):
                matrix[rownumber][j]=0
                
        for colnumber in affect_col:
            for j in range(r):
                matrix[j][colnumber]=0
                
        
        
                    
        