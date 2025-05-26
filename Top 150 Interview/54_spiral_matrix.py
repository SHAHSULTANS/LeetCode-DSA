


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:        
        row=len(matrix)
        col=len(matrix[0])
        r1=0
        r2=row-1
        c1=0
        c2=col-1
        ans=[]
        
        while(r2>=r1 and c2>=c1):
            #left to right
            if r2-r1>=0:
                for top_row_print in range(c1,c2+1):
                    ans.append(matrix[r1][top_row_print])
                    # print(matrix[r1][top_row_print], end=" ")
            
            #top to bottom
            if r2-r1>1:
                for top_to_bottom in range(r1+1,r2):
                    ans.append(matrix[top_to_bottom][c2])
                    # print(matrix[top_to_bottom][c2],end=" ")
            # print("stop")

            #right to left
            if r2-r1>0:
                for bottom_row_print in range(c2,c1-1,-1):
                    # print(matrix[r2][bottom_row_print],end=" ")
                    ans.append(matrix[r2][bottom_row_print])
            
            #bottom to top
            if r2-r1>1 and c2-c1>0:        
                for bottom_to_up in range(r2-1,r1,-1):
                    ans.append(matrix[bottom_to_up][c1])
                    # print(matrix[bottom_to_up][c1],end=" ")
                    
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        
        return ans
        
        # for i in range((row+1)//2):
            
        #     for j in range(i,col-i):
        #         ans.append(matrix[i][j])
                
        #         # print(matrix[i][j], end=" ")
        #     # print(j)
        #      #top to down
        #     if row-i-i-1>0:
        #         tr=i+1
        #         for k in range (tr,row-i):
        #             ans.append(matrix[k][k])
                    
        #             # print(matrix[k][j], end=" ")    

        #         #right to left
        #         rc=j-1
        #         for m in range (rc,i-1,-1):
        #             ans.append(matrix[k][m])
                    
        #             # print(matrix[k][m],end=" ")  
        #             # pass
        #         #bottom to top
        #         br=k-1
        #         for n in range(br,i,-1):
        #             ans.append(matrix[n][m])
        #             # print(matrix[n][m],end=" ")
        #             # pass
        
        # return ans