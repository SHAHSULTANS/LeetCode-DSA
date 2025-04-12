from pyparsing import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses

        create_graph=[[] for _ in range(numCourses)]
        for item in prerequisites:
            create_graph[item[1]].append(item[0])
            indegree[item[0]]+=1

        

        # for edgelist in create_graph:
        #     for edge in edgelist:
        #         indegree[edge]+=1
                # print(edge," ",len(indegree))

            # print()

        q=deque()
        for index,x in enumerate(indegree):
            if x==0:
                q.append(index)
                
        ans=[]

        # print(q)
        
        while q:
            # print("YES")
            item=q.popleft()
            # print(create_graph[item])
            ans.append(item)
            
            for edge in create_graph[item]:
                indegree[edge]-=1
                if indegree[edge]==0:
                    q.append(edge)
                        
        if len(ans)==numCourses:
            return True
        
        return False
                
        
        
        
        
    
        # print(indegree)
        # print(create_graph)
        