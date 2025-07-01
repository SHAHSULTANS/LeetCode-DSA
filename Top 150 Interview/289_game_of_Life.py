


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.row=len(board)
        self.col=len(board[0])

        track = copy.deepcopy(board)



        
        def calcuate_negibors(i,j):
            directions =[(-1, -1), (-1, 0), (-1, 1),
                        ( 0, -1),          ( 0, 1),
                        ( 1, -1), ( 1, 0), ( 1, 1)]
            
            game_counter={}

            for dx, dy in directions:
                ni=i+dx
                nj=j+dy
                # print(ctn)
                
                if 0<=ni<self.row and 0<=nj<self.col:
                    # if i==1 and j==1: 
                    #     print(ni," ",nj,"---->",board[ni][nj])
                    game_counter[board[ni][nj]]=game_counter.get(board[ni][nj],0)+1
                    
            # if i==1 and j==1:
            #     print(game_counter)
            return game_counter.get(1,0)
            
            # return game_counter.get(0,0)


        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                dicison=calcuate_negibors(i,j)

                # print(dicison)
                
                if board[i][j]==1:
                    if dicison<2:
                        track[i][j]=0
                    elif dicison>3:
                        track[i][j]=0
                else:
                    if dicison==3:
                        track[i][j]=1
                        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=track[i][j]                
            
                
        
             
            
             
                    
        
        