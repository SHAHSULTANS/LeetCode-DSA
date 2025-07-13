
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
           
            j=i+1
            # index=j
            while(j<n):

                k=j+1
                m=n-1

                while k<m:
                    # if nums[j]==nums[j+1]:
                    #     j+=1
                    #     continue
                    # if nums[k]==nums[k-1]:
                    #     k-=1
                    #     continue
                    
                    summation=nums[i]+nums[j]+nums[k]+nums[m]
                    # print(summation)
                    
                    if summation==target:
                        ans.append([nums[i],nums[j],nums[k],nums[m]]) 
                        # while j<n and nums[j]==nums[j+1]:

                        while k<m and nums[k]==nums[k+1]:
                        
                            k+=1

                        while  k<m and nums[m]==nums[m-1]:
                            m-=1


                        
                    if summation<target:
                        k+=1
                    else:
                        m-=1


                j+=1
                while j<n and nums[j]==nums[j-1]:
                    j+=1
                    
        return ans


# 📌 LeetCode 18: Four Sum Problem

# ✅ বাস্তব জীবনের অ্যাপ্লিকেশনসমূহ

# 🧾 উদাহরণ: তোমার কাছে সংখ্যাগুলোর একটা তালিকা আছে
# nums = [1, 0, -1, 0, -2, 2]
# এবং তুমি খুঁজতে চাও কোন চারটি সংখ্যা মিলে sum = 0 হয়।

# ✅ 1. 🧾 Financial Fraud Detection
# চারটি লেনদেনের যোগফল যদি suspiciously 0 হয় (e.g. money laundering)
# ➤ একাধিক ট্রান্সাকশন net result করে hide করা হয়

# ✅ 2. 🧪 Chemical Reaction Simulation
# চারটি মৌলিক পদার্থের শক্তি যোগফল = নির্দিষ্ট value (target) হলে reaction হয়
# ➤ chemical balancing বা catalyst combination modeling

# ✅ 3. 📦 Inventory Bundle Recommendation
# চারটি পণ্যের দাম মিলিয়ে ঠিক নির্দিষ্ট বাজেটের মধ্যে ফেলা
# ➤ e.g. Pick 4 items that sum to $100

# ✅ 4. 📈 Risk Allocation Across 4 Assets
# ➤ 4টি asset মিলে নির্দিষ্ট profit/loss constraint পূরণ করে কিনা check করা

# ✅ 5. 🎮 Game Character Power Balancing
# ➤ একটি টিমে চারজন প্লেয়ারের শক্তির যোগফল নির্দিষ্ট মাত্রায় রাখতে হবে

# ❌ না থাকলে:
# - Refund mismatch detect করা যাবে না
# - Product combo suggestion fail করবে
# - Game balancing বা AI strategy ভুল হবে
