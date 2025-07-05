from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        fresh=0
        q=deque()
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j,0))

        ans=0

        # print(fresh)         
        while q:
            rooten=q.popleft()
            i,j,k=rooten[0],rooten[1],rooten[2]
            
            if i-1>=0 and grid[i-1][j]==1:
                grid[i-1][j]=2
                q.append((i-1,j,k+1))
                fresh-=1
                ans=max(ans,k+1)
                
            if i+1<row and grid[i+1][j]==1:
                grid[i+1][j]=2
                q.append((i+1,j,k+1))
                fresh-=1
                ans=max(ans,k+1)

                
            #for col
            if j-1>=0 and grid[i][j-1]==1:
                grid[i][j-1]=2
                q.append((i,j-1,k+1))
                fresh-=1
                ans=max(ans,k+1)

                
            if j+1<col and grid[i][j+1]==1:
                grid[i][j+1]=2
                q.append((i,j+1,k+1))
                fresh-=1
                ans=max(ans,k+1)

                
        if fresh:
            return -1

        return ans

        
        
# 📌 বাস্তব জীবনের ব্যবহার (Real-World Applications of Rotting Oranges Problem)
# ✅ Problem: এক ধরণের BFS (Breadth-First Search) যেখানে একটি অবস্থা চারদিকে ছড়ায় প্রতি ইউনিট টাইমে।

# ✅ ১. রোগ ছড়ানো (Disease Spread Simulation)
# উদাহরণ: একটি শহরে একজন করোনা রোগী আছে। সে প্রতিদিন চারপাশের লোকদের সংক্রমিত করে।
# grid[i][j] = 1 → সুস্থ লোক, 2 → আক্রান্ত লোক
# এই অ্যালগরিদম বলে কতদিনে পুরো শহর সংক্রমিত হবে।
# ব্যবহার: করোনার মতো মহামারির সময় সংক্রমণের গতি নির্ধারণ, কন্টেইনমেন্ট জোন তৈরি।

# ✅ ২. আগুন ছড়ানো (Forest Fire Simulation)
# উদাহরণ: একটি গাছে আগুন ধরেছে, প্রতি ঘন্টায় সেটি পাশের গাছে ছড়ায়।
# grid[i][j] = 1 → শুকনা গাছ, 2 → জ্বলন্ত গাছ
# ব্যবহার: ফায়ার ফাইটারদের আগুনের ছড়িয়ে পড়া অনুমান করা, এভাকুয়েশন প্ল্যান তৈরি করা।

# ✅ ৩. ভাইরাস ছড়ানো কম্পিউটার নেটওয়ার্কে (Network Virus Propagation)
# উদাহরণ: একটি কম্পিউটার ভাইরাস পাশের ডিভাইসে ছড়ায় প্রতি মিনিটে।
# ব্যবহার: সাইবার আক্রমণের গতি বুঝা, নিরাপত্তা পরিকল্পনা বানানো।

# ✅ ৪. পণ্যের নষ্ট হওয়া (Warehouse Spoilage)
# উদাহরণ: একটি খাবার পঁচে গেলে তার পাশে থাকা বাক্সগুলোও নষ্ট হয়ে যায়।
# ব্যবহার: স্টোরে inventory spoilage model করা, automation এর মাধ্যমে সরানো।

# ✅ ৫. বন্যা বা তেল ছড়ানো (Flood/Oil Spill Simulation)
# উদাহরণ: একটি ঘরে পানি ঢোকে, ধীরে ধীরে পাশের ঘরে যায়।
# ব্যবহার: বন্যা এলাকা নির্ণয়, cleaning robot-এর পথ বের করা।

# ✅ ৬. ক্লাউড সার্ভারে ডেটা ছড়ানো (Message Broadcasting in Systems)
# উদাহরণ: একটি সার্ভার প্রতি সেকেন্ডে পাশের ৪টি সার্ভারে ডেটা পাঠায়।
# ব্যবহার: distributed system design, latency নির্ণয়।

# ✅ সারাংশ:
# যে কোন সমস্যা যেখানে "একটা ঘটনা চারপাশে ছড়ায় এক ধাপে" — সেগুলোতে এই টাইপ BFS অ্যালগরিদম বাস্তবে খুবই দরকারি।
