from unittest import result


class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=3:
            return max(nums)
        
        def profit(ar):
            
            
            ans=[]
            ans.append(ar[0])
            ans.append(ar[1])
            ans.append(ar[0]+ar[2])
            for i in range(3,len(ar),1):
                summation=max(ar[i]+ans[i-2],ar[i]+ans[i-3])
                ans.append(summation)
                
            return max(ans[-1],ans[-2])
        
        
        
        return max(profit(nums[0:n-1]),profit(nums[1:n]))
                
            
       
                
        
        

        # #we may include last house or not if result come from first house.
        # if ans[-1][1]==0:
        #     a=ans.pop()
        #     profit=a[0]
        #     if nums[0]>nums[-1]:
        #         profit-=nums[-1]
        #     else:
        #         profit-=nums[0]
                
        #     ans.append((profit,0))
                
        # return max(ans[-1][0],ans[-2][0])
        
        
        
        
        
        
# =============================================
# 🏡 Leetcode 213: House Robber II - Real Life Applications
# =============================================

# ✅ সমস্যার সারাংশ:
# একটি সার্কুলার এলাকার বাড়িগুলোর মধ্যে চুরি করতে হবে এমনভাবে যেন
# কোন দুটি পাশাপাশির বাড়ি থেকে চুরি না হয়।
# লক্ষ্য: সর্বোচ্চ পরিমাণ টাকা (বা সুবিধা) পাওয়া।

# 🔁 এই প্রবলেমের কাঠামো:
# - প্রতিটি item এর value আছে
# - পাশাপাশি দুটো item একসাথে নেওয়া যাবে না
# - array টি circular (প্রথম ও শেষ পরস্পরের প্রতিবেশী)

# =============================================
# 📱 Application 1: Smartphone Battery Optimization
# ---------------------------------------------
# - কিছু background task আছে যেগুলো চালু রাখলে উপকার পাওয়া যায়।
# - প্রতিটি task এর একটি value (importance/utility) আছে।
# - কিন্তু পাশাপাশি দুটি টাইমস্লট চালু রাখলে ব্যাটারি drain হয়।
# - দিনের শুরু ও শেষ টাইমস্লট সংযুক্ত (circular day cycle)।
# - লক্ষ্য: কোন টাইমস্লটগুলো চালু রাখা হবে যাতে সর্বোচ্চ utility পাওয়া যায়?
# - এই সমস্যাটি House Robber II এর মতো।

# =============================================
# 🏥 Application 2: Hospital Nurse Shift Scheduling
# ---------------------------------------------
# - নার্সদের সপ্তাহে 7 দিনের শিডিউল বানাতে হবে।
# - কোনো নার্স পরপর দুইদিন কাজ করতে পারবে না (পরিশ্রমের সীমা)।
# - প্রতিটি দিনের shift এর score আছে (workload বা criticality অনুযায়ী)।
# - সপ্তাহটি circular (শনিবার ও রবিবার পরপর ধরা হয়)।
# - লক্ষ্য: নার্সদের জন্য এমন শিডিউল তৈরি করা যাতে সর্বোচ্চ coverage হয়।

# =============================================
# 🏘️ Application 3: Village Development Project Allocation
# ---------------------------------------------
# - কিছু গ্রামে উন্নয়ন প্রকল্প দেওয়া হবে।
# - প্রতিটি গ্রামে প্রকল্প দিলে একটি সুবিধা (score) পাওয়া যায়।
# - পাশাপাশি দুটি গ্রামে একসাথে প্রকল্প দেওয়া যাবে না (resource conflict)।
# - গ্রামগুলো একটি গোল চক্রে সাজানো (circular map)।
# - লক্ষ্য: কোন গ্রামে প্রকল্প দিলে সর্বোচ্চ উন্নয়ন সুবিধা পাওয়া যাবে?

# =============================================
# 🎓 Application 4: Course Scheduling with Conflicts
# ---------------------------------------------
# - কিছু কোর্স আছে যেগুলোর মধ্যে conflict relationship আছে।
# - কোর্সগুলো circular timetable-এ দেয়া।
# - পাশাপাশি দুটি conflict কোর্স একসাথে নেওয়া যাবে না।
# - প্রতিটি কোর্সের value (importance/credit) আছে।
# - লক্ষ্য: এমন কোর্স নির্বাচন করা যাতে সর্বোচ্চ ক্রেডিট পাওয়া যায়।

# =============================================
# ✅ এই ধরনের সব সমস্যা House Robber II এর মতো দেখা যায়
# যেখানে "neighbor conflict" + "circular dependency" থাকে।
