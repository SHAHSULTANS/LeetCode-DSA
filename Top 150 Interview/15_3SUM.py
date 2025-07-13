
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
           
            j=i+1
            k=n-1
            while j<k:
                # if nums[j]==nums[j+1]:
                #     j+=1
                #     continue
                # if nums[k]==nums[k-1]:
                #     k-=1
                #     continue
                
                summation=nums[i]+nums[j]+nums[k]
                
                if summation==0:
                    ans.append([nums[i],nums[j],nums[k]]) 

                    while j<k and nums[j]==nums[j+1]:
                    
                        j+=1

                    while j<k and nums[k]==nums[k-1]:
                        k-=1


                      
                if summation<0:
                    j+=1
                else:
                    k-=1
                    
        return ans


# 📌 LeetCode 15: Three Sum Problem
# -----------------------------------------------
# 🎯 উদ্দেশ্য: এমন তিনটি সংখ্যা খুঁজে বের করা যাদের যোগফল = 0
# উদাহরণ: [-3, 1, 2] → sum = 0

# -----------------------------------------------
# ✅ বাস্তব জীবনের অ্যাপ্লিকেশন (Real-World Applications)
# -----------------------------------------------

# 💰 1. Transaction Matching System
# Example: transactions = [-50, 20, 30]
# ➤ ৫০ টাকা গিয়েছে, ২০ ও ৩০ টাকা পেয়েছে — সব মিলিয়ে ০
# ➤ ব্যাংক বা হিসাব সফটওয়্যারে refund বা কাটাকাটি যাচাই

# ❌ Without it:
# - ভুল হিসাব detect হবে না
# - Fraud বা double payment ধরতে পারবে না

# 🛒 2. Shopping Combo Offer Matching
# Example: prices = [-30, 10, 20] → Total = 0
# ➤ কম্বো অফার যেখানে ৩টি প্রোডাক্ট মিলে অফার হয় (e.g., free combo)
# ➤ E-commerce সাইটে backend combo checker হিসেবে ব্যবহার

# ❌ Without it:
# - ডিসকাউন্ট ভুল হবে
# - ইউজার ফ্রি অফার মিস করবে → user frustration

# ⚗️ 3. Chemical Reaction Energy Balance
# Example: energies = [-2, 1, 1]
# ➤ রিএকশনের সময় total energy = 0 করতে হয় → balanced equation
# ➤ Science simulation tools এ ব্যবহৃত

# ❌ Without it:
# - ভুল রিএকশন দেখা যাবে
# - শিক্ষার্থীরা ভুল শিক্ষা পাবে

# 📈 4. Investment Risk Neutral Portfolio Detection
# Example: gains = [-3, 1, 2]
# ➤ একটার loss আর বাকি দুইটার gain → total = 0
# ➤ Portfolio app গুলো বলে দেয় কোন combination balanced

# ❌ Without it:
# - Wrong suggestion দিবে
# - Risk calculation fail করবে → টাকা হারাবে

# 🎮 5. Game Character Team Balance
# Example: powers = [-2, 1, 1]
# ➤ একজন defender (-2) আর দুইজন attacker (+1) → team balanced
# ➤ Fair gameplay balance করতে ব্যবহার হয়

# ❌ Without it:
# - একদল খুব strong, আরেক দল দুর্বল হবে
# - Game unfair → player frustration → uninstall

# 🧠 6. AI Planning & Conflict Resolution
# Example: decisions = [2, -1, -1] → total = 0
# ➤ AI এমন সিদ্ধান্ত নেয় যাতে মোট ফলাফল neutral হয়
# ➤ Constraint satisfaction problems এ ব্যবহৃত

# ❌ Without it:
# - AI ভুল সিদ্ধান্ত নেবে
# - Conflict resolution fail করবে

# -----------------------------------------------
# ✅ উপসংহার:
# যেখানেই তিনটি উপাদান মিলে একটি নিরপেক্ষ বা নির্দিষ্ট ফলাফল (যেমন 0) অর্জন করতে হয় —
# সেখানে `Three Sum` algorithm ব্যবহার করে সঠিক সমাধান করা যায়।

# ❌ যদি ব্যবহার না করো:
# - Business logic fail হবে
# - Refund, discount, balance, fairness ইত্যাদি সব ভুল হবে
# - System trust হারাবে, performance কমবে
