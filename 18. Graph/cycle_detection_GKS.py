class Solution:
    def isCycle(self, V, edges):
        adjacent_list = [[] for _ in range(V)]
        for edge in edges:
            adjacent_list[edge[0]].append(edge[1])
            
        # print(adjacent_list)    
            
        visited=[0]*V   
        # print(visited)
        self.hascycle=False
        
        def dfs(node):
            # print(visited)
            if visited[node]==1:
                # print("cycle")
                self.hascycle=True
                return
            
            # print(visited[node]," node ",node)
            
            visited[node]=1
            
            for neighbour in adjacent_list[node]:
                # print("parent: ",node," neighbor", neighbour)
                # if visited[neighbour]==0:
                dfs(neighbour)
            
            # print(node)
            visited[node]=2
            
        for node in range(V):
            if visited[node]==0:
                dfs(node)
                
        
        return self.hascycle
            
 
 
 
 
 
#Efficient Solution, Early return if cycle exists.        
class Solution:
    def isCycle(self, V, edges):
        adjacent_list = [[] for _ in range(V)]
        for u, v in edges:
            adjacent_list[u].append(v)

        visited = [0] * V  # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(node):
            visited[node] = 1
            for neighbour in adjacent_list[node]:
                if visited[neighbour] == 1:
                    return True  # found a back edge (cycle)
                if visited[neighbour] == 0:
                    if dfs(neighbour):
                        return True
            visited[node] = 2
            return False

        for node in range(V):
            if visited[node] == 0:
                if dfs(node):  # ✅ early exit on cycle
                    return True
        return False



# ✅ Directed Graph Cycle Detection এর রিয়েল ওয়ার্ল্ড অ্যাপ্লিকেশনসমূহ (বাংলায়):

# ১. Course Prerequisite Validation (Topological Sort):
#    যদি কোনো কোর্স অন্য একটি কোর্সের ওপর নির্ভর করে এবং সেখান থেকে আবার আগেরটিতে ফিরে যায় (cycle),
#    তাহলে সেই কোর্স প্ল্যান সম্ভব নয় — এ ক্ষেত্রে cycle detection দিয়ে validate করা হয়।

# ২. Deadlock Detection in Operating Systems:
#    বিভিন্ন প্রসেস ও রিসোর্সের dependency গুলো Directed Graph আকারে থাকে।
#    যদি cycle পাওয়া যায়, তাহলে deadlock হয়েছে — system হ্যাং করতে পারে।

# ৩. Build Systems (Makefile / CI pipelines):
#    ফাইল বা টাস্কগুলো যদি পরস্পরের ওপর নির্ভর করে, তাহলে cycle detect করে circular dependency রোধ করা হয়।

# ৪. Version Control Systems (e.g., Git):
#    Merge operation বা commit graph traversal-এ directed acyclic structure নিশ্চিত করতে হয়।

# ৫. Package Dependency Management (npm, pip):
#    কোনো প্যাকেজ যদি অন্য একটি প্যাকেজের ওপর নির্ভর করে এবং সেটিও আবার প্রথমটিতে — তখন cycle detect করতে হয়।

# ৬. Workflow Engines / Task Scheduling Systems:
#    Directed Graph-এ কাজগুলো সাজানো থাকে; cyclic dependency থাকলে কাজ সম্পূর্ণ করা সম্ভব নয়।

# ৭. Compiler Design (Symbol Dependency Analysis):
#    ফাংশন বা ভেরিয়েবল ডিপেন্ডেন্সি অ্যানালাইসিসে cycle থাকলে সেটি error ধরা হয়।

# ৮. Circuit Design & Analysis:
#    Logic gate বা data flow-এ feedback loops (cycles) অনেক সময় detect করতে হয়।

# 🔁 সংক্ষেপে: কোনো system বা process যদি Directed dependency follow করে, সেখানে cycle detection গুরুত্বপূর্ণ।
