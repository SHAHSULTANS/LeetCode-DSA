
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
    
        ans=[]
        
        def dfs(ar,index):
            if len(ar)==k:
                ans.append(ar.copy())
                return
                
            
            for i in range(index,n+1,1):
                ar.append(i)
                dfs(ar,index+1)
                index+=1
                ar.pop()
                
            return
        
        dfs([],1)
        return ans
        
        
# ✅ ১. 🔐 Security Systems / Password Generator
# অনেক character থেকে নির্দিষ্ট সংখ্যক combination খুঁজে বের করে password তৈরি করতে ব্যবহার হয়।
# Example: 6টি অক্ষর থেকে 3-character-এর password: combinations(6, 3) = 20 সম্ভাব্য পাসওয়ার্ড।

# ✅ ২. 🧪 Software Testing (Test Case Coverage)
# Input field এর সম্ভাব্য combination দিয়ে system কে বিভিন্ন input scenario-তে test করা হয়।
# Example: Browser (3), OS (2), Network (2) → combinations of these = exhaustive test cases।

# ✅ ৩. 🧠 Recommendation Systems
# E-commerce বা streaming site-এ product বা content combination সাজেস্ট করতে ব্যবহৃত হয়।
# Example: "People who bought A also bought B & C" → combinations of items.

# ✅ ৪. 📦 Inventory & Package Management
# Warehouse বা packaging system বিভিন্ন item দিয়ে bundle তৈরি করে এবং combinations ব্যবহার করে best set খুঁজে বের করে।
# Example: Combo Pack (Rice, Oil, Salt), (Shampoo, Soap, Toothpaste)

# ✅ ৫. 🎮 Game Development
# Game character এর জন্য skill বা weapon এর combination গঠন করতে ব্যবহৃত হয়।
# Example: একটি player 5টি power থেকে 2টি নিতে পারবে → power combinations তৈরি হয়।

        