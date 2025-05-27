class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r1=0
        r2=n-1
        c1=0
        c2=n-1
        ans=[]
        ans=[[0]*n for _ in range(n)]
        count=1
        
        while(r2>=r1 and c2>=c1):
            #left to right
            if r2-r1>=0:
                for top_row_print in range(c1,c2+1):
                    ans[r1][top_row_print]=count
                    count+=1
                    # ans.append(matrix[r1][top_row_print])
                    # print(matrix[r1][top_row_print], end=" ")
            
            # print(ans)
            # break
            #top to bottom
            if r2-r1>1:
                for top_to_bottom in range(r1+1,r2):
                    ans[top_to_bottom][c2]=count
                    count+=1
                    # ans.append(matrix[top_to_bottom][c2])
                    # print(matrix[top_to_bottom][c2],end=" ")

            # print(ans)

            #right to left
            if r2-r1>0:
                for bottom_row_print in range(c2,c1-1,-1):
                    ans[r2][bottom_row_print]=count
                    count+=1
                    # print(matrix[r2][bottom_row_print],end=" ")
                    # ans.append(matrix[r2][bottom_row_print])
            # print(ans)
            
            #bottom to top
            if r2-r1>1 and c2-c1>0:        
                for bottom_to_up in range(r2-1,r1,-1):
                    ans[bottom_to_up][c1]=count
                    count+=1
                    # ans.append(matrix[bottom_to_up][c1])
                    # print(matrix[bottom_to_up][c1],end=" ")
            # print(ans)


            # print()        
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        
        return ans