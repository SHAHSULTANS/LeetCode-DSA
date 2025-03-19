

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        
        row=len(matrix)
        col=len(matrix[0])
        
        for i in range((row+1)//2):
            
            for j in range(i,col-i):
                ans.append(matrix[i][j])
                
                # print(matrix[i][j], end=" ")
            # print(j)
             #top to down
            if row-i-i-1>0:
                tr=i+1
                for k in range (tr,row-i):
                    ans.append(matrix[k][k])
                    
                    # print(matrix[k][j], end=" ")    

                #right to left
                rc=j-1
                for m in range (rc,i-1,-1):
                    ans.append(matrix[k][m])
                    
                    # print(matrix[k][m],end=" ")  
                    # pass
                #bottom to top
                br=k-1
                for n in range(br,i,-1):
                    ans.append(matrix[n][m])
                    # print(matrix[n][m],end=" ")
                    # pass
        
        return ans