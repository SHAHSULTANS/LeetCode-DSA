"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #One pass bfs
        if node:
            node_map={}
            q=deque()
            q.append(node)
            rt=node_map[node]=Node(node.val)

            
            while q:
                # print(q)
                # print("q above")
                font=q.popleft()

                
                for adjacent in font.neighbors:
                    if node_map.get(adjacent) is None:
                        # print("adj ",adjacent.val)
                        q.append(adjacent)
                        node_map[adjacent]=Node(adjacent.val)
                        
                    node_map[font].neighbors.append((node_map[adjacent]))
                    # print(font.val,"----------->adj-->", adjacent.val)
                    # print(node_map[font].neighbors)

            # rt=node_map[node]
            # print(rt)
            return rt



# 📌 LeetCode 133 - Clone Graph এর বাস্তব জীবনের ব্যবহার (Real-World Applications in Bangla)
# ------------------------------------------------------------------------------
# 🧠 Clone Graph মূলত ব্যবহার হয় যেখানে graph বা network structure কে
# মূল system touch না করে আলাদা করে কপি করে কাজে লাগাতে হয়।
# ------------------------------------------------------------------------------

# ✅ ১. Social Network Graph Simulation
# উদাহরণ: Facebook/LinkedIn-এর ইউজার নেটওয়ার্ককে কপি করে friend suggestion engine চালানো।
# মূল গ্রাফ না বদলে test বা model করতে clone করা হয়।
# ব্যবহার:
# - Friend Recommendation
# - Privacy-preserving Graph Analysis
# - Graph AI Training

# ✅ ২. Multiplayer Game Map Isolation (e.g. PUBG, Free Fire)
# উদাহরণ: Free Fire-এ প্রতিটি প্লেয়ারের জন্য একই map, কিন্তু আলাদা instance/cloned world
# clone ছাড়া একজনের action অন্যজনের map-এ reflect করতে পারে!
# ব্যবহার:
# - Custom Room per player
# - Replay system with isolated world
# - AI bot-specific path graph

# ✅ ৩. Workflow / Diagram Editor (e.g. Node-RED, Unreal Blueprints)
# উদাহরণ: ইউজার visual editor-এ flowchart বা data pipeline বানায়।
# যখন সে undo/redo/save করে, তখন মূল graph কে clone করে রাখা হয়।
# ব্যবহার:
# - Undo/Redo implementation
# - Autosave snapshots
# - Version history comparison

# ✅ ৪. Distributed System Testing
# উদাহরণ: একটি সার্ভার গ্রাফে অনেক সার্ভার ও তাদের dependency রয়েছে।
# এই গ্রাফ কে clone করে fail-over simulation চালানো হয়।
# ব্যবহার:
# - Fault-tolerant system simulation
# - Safe testing environment
# - Dependency update without side effect

# ✅ ৫. AI Agent Planning
# উদাহরণ: AI bot একটি গ্রাফ structure-এ কাজ করে। একাধিক bot কে isolate করার জন্য clone করা হয়।
# clone না করলে এক bot-এর decision অন্য bot কে affect করে দিতে পারে।
# ব্যবহার:
# - Pathfinding
# - Multi-agent simulation
# - Reinforcement Learning environments

# ✅ ৬. Knowledge Graph Query Isolation
# উদাহরণ: একজন ইউজার যখন একটি query চালায় (e.g., "Shanto is a developer")
# তখন graph-এর এক টুকরো অংশ clone করে query apply করা হয়, যাতে মূল graph corrupt না হয়।
# ব্যবহার:
# - Temporary context creation
# - Ontology modification
# - Safe Semantic Search

# ✅ ৭. Replay System in Games
# উদাহরণ: PUBG-এর KillCam বা Replay feature → ম্যাচ শেষ হবার সময় পুরো game world clone করা হয়
# clone না করলে live ম্যাচ-এর সাথে conflict হতো।
# ব্যবহার:
# - Replay review
# - KillCam animation
# - Game analytics

# ✅ ৮. Developer Test Environments
# উদাহরণ: গেম ডেভেলপার যখন নতুন bug fix বা AI behavior test করে,
# তখন মূল game map/graph কে clone করে আলাদাভাবে run করে।
# ব্যবহার:
# - Level testing
# - Bug reproduction
# - A/B testing

# ------------------------------------------------------------------------------
# 🧨 যদি clone করা না হয়:
# - Shared reference bug হয়ে যাবে
# - Undo/Redo system কাজ করবে না
# - AI agents একে অপরকে affect করবে
# - Replay চালালে live game corrupt হবে
# ------------------------------------------------------------------------------

# ✅ Clone Graph = নিরাপদ, isolate করা, পরিবর্তনযোগ্য পরিবেশ
# ✅ Clone করা মানে হলো — test করো, দেখো, শেখো — কিন্তু আসল জিনিস নষ্ট না করো 😎
 
 
                
#___________________________Two pass dfs bfs___________________________________________        
        
        
        # return node
        # if node:
        #     node_map={}
        #     visited={}
        #     q=deque()
        #     q.append(node)
        #     node_map[node]=Node(node.val)
            
        #     while q:
        #         # print(q)
        #         # print("q above")
        #         font=q.popleft()
        #         visited[font]=True

                
        #         for adjacent in font.neighbors:
        #             if visited.get(adjacent) is None:
        #                 q.append(adjacent)
        #                 node_map[adjacent]=Node(adjacent.val)
                        
        #             node_map[font].neighbors.append(Node(adjacent.val))
        #             print(font.val)
        #             print(node_map[font].neighbors)
                
        #     rt=(node_map[node])

        #     return rt
                
            
                        
                

        