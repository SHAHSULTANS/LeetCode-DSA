class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def dfs(ar):
            if len(ar)==n:
                ans.append(ar)
                return
            
            for item in nums:
                if ar.count(item)==0:
                    cp=ar.copy()
                    cp.append(item)
                    dfs(cp)
                
        
        dfs([])
        return ans
    

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        visited=[False]*n
        def dfs(ar):
            if len(ar)==n:
                ans.append(ar.copy())
                return
            
            for i in range(n):
                item=nums[i]
                if visited[i]==False:
                    visited[i]=True
                    ar.append(item)
                    dfs(ar)
                    ar.pop()
                    visited[i]=False
                
        
        dfs([])
        return ans




# ✅ পারমুটেশনের রিয়েল ওয়ার্ল্ড অ্যাপ্লিকেশনসমূহ (বাংলায়):

# ১. Scheduling বা Task Assignment:
#    উদাহরণ: ৪টি কাজ ৪জন কর্মীর মধ্যে কতভাবে ভাগ করা যায় → পারমুটেশন

# ২. Password Cracking বা Brute Force:
#    সম্ভাব্য সব পাসওয়ার্ড কম্বিনেশন চেষ্টা করার সময় permutation ব্যবহার হয়

# ৩. Puzzle বা Game Solver:
#    যেমন: Sudoku, tile puzzle, word jumble — সব সম্ভাব্য configuration চেক করতে হয়

# ৪. Anagram Generator:
#    একটি শব্দের সব ভিন্ন arrangement তৈরি করতে ব্যবহৃত হয়

# ৫. Small Scale Optimization Problems:
#    যেমন: Traveling Salesman Problem (TSP) — সব path permutation evaluate করা হয়

# ৬. Cryptography:
#    Key generation, encoding–এ বিভিন্ন bit/character arrangement দরকার হয়

# ৭. Test Case Generation:
#    Automation-এ সব input ordering/permutation চেক করা হয় bugs ধরার জন্য

# ৮. Seating Arrangements:
#    কতভাবে ৪ জন মানুষকে ৪টি চেয়ারে বসানো যায় — পারমুটেশন

# ৯. Robotics Path Planning:
#    বিভিন্ন কাজের order নির্ধারণে permutation ব্যবহার করা হয়

# 🔁 সবগুলোই বাস্তবে নানা রকম ডেটা অর্ডারিং এবং optimization এর ক্ষেত্রে কাজে লাগে।
