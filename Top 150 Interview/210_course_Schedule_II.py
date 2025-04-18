from unittest import result
from pyparsing import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        self.create_graph=[[] for _ in range(numCourses)]
        for item in prerequisites:
            self.create_graph[item[1]].append(item[0])
        #     indegree[item[0]]+=1

        
        self.res=[]
        self.visisted=[0]*numCourses
        self.cycle=False
        
        
        def dfs(node):
            
            if self.visisted[node]==1:
                self.cycle=True
                return
            
            if self.visisted[node]==2:
                return
            
            self.visisted[node]=1
            
            for neighbour in self.create_graph[node]:
                dfs(neighbour)
            
            self.visisted[node]=2
                
            self.res.append(node)
            
            
        for node in range(numCourses):
            if self.visisted[node]==0:
                dfs(node)
                
        if self.cycle:
            return []
        
        return self.res[::-1]
            
        

        # # for edgelist in create_graph:
        # #     for edge in edgelist:
        # #         indegree[edge]+=1
        #         # print(edge," ",len(indegree))

        #     # print()

        # q=deque()
        # for index,x in enumerate(indegree):
        #     if x==0:
        #         q.append(index)
                
        # ans=[]

        # # print(q)
        
        # while q:
        #     # print("YES")
        #     item=q.popleft()
        #     # print(create_graph[item])
        #     ans.append(item)
            
        #     for edge in create_graph[item]:
        #         indegree[edge]-=1
        #         if indegree[edge]==0:
        #             q.append(edge)
                        
        # if len(ans)==numCourses:
        #     return ans
        
        # return []
                
        
        
        
        
    
        # # print(indegree)
        # # print(create_graph)
        