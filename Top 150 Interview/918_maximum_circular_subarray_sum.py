class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for item in nums:
            current_sum=max(item,current_sum+item)
            max_sum=max(max_sum,current_sum)

        # return max_sum
        min_sum=nums[0]
        current_sum=0
        # print(max_sum)

        for item in nums:
            current_sum=min(item,current_sum+item)
            min_sum=min(min_sum,current_sum)
        
        total=sum(nums)
        if total-min_sum==0:
            return max_sum

        return max(max_sum,(total-min_sum))

# 📌 LeetCode 918 - Maximum Sum Circular Subarray
# 🎯 বাস্তব জীবনের অ্যাপ্লিকেশনসমূহ (Real-World Applications in Bangla)

# ✅ ১. 🔋 Battery Usage Optimization (Smartwatch, Smartphone)
# উদাহরণ: charge_log = [3, -2, 5, -4, 2, -1]
# Positive মানে charge, Negative মানে drain
# Circular ধরার কারণ: রাত থেকে সকাল পর্যন্ত usage pattern detect করতে হয়
# ব্যবহার:
# - Sleep mode optimization
# - Smart charging suggestion
# - Battery drain hotspot analysis

# ✅ ২. 🏭 Conveyor Belt Load Monitoring
# উদাহরণ: belt_load = [5, -6, 3, -2, 4]
# Factory তে belt ঘুরে ফিরে আসে, তাই circular consideration দরকার
# ব্যবহার:
# - Most efficient segment খুঁজে শুরু করতে
# - Predictive maintenance
# - Load balancing

# ✅ ৩. 🛰️ Satellite Signal Strength Optimization
# উদাহরণ: signal_strength = [-1, 3, -2, 4, -3, 2]
# Satellite পৃথিবীকে একবার ঘুরে আসে → circular orbit ধরে
# ব্যবহার:
# - Best signal window খুঁজে transmission করা
# - Dead zone এড়ানো
# - Transmission success rate বাড়ানো

# ✅ ৪. 🎮 Game Engine Frame Heat Detection
# উদাহরণ: frame_heat = [20, -10, 30, -5, -25, 40]
# Game engine এ frame rendering একটি cyclic (circular) loop এ চলে
# ব্যবহার:
# - Frame drop বা heat buildup detect করা
# - Lag prediction
# - Frame scheduling optimization

# ✅ ৫. 📈 Stock Market Cross-day Trend Detection
# উদাহরণ: stock_movement = [-2, 3, -1, 4, -3, 5, -2]
# Market গত এক সপ্তাহের data circular ধরে: শুক্রবার বিকেলে কিনে সোমবার সকালে বিক্রি
# ব্যবহার:
# - Highest profit window খুঁজে বের করা
# - Buy/sell suggestion
# - Automated trading strategy design

# 🔁 কেন Circular ধরতে হয়:
# - Data শেষ হয়ে আবার শুরু হয় (Day → Night → Day)
# - Real-world systems often work in loops (24hr, weekly, orbital, etc.)
# - শুধুমাত্র Kadane’s algorithm দিলে circular edge cases মিস হয়

# ✅ যদি এই logic না ব্যবহার করো:
# - Battery usage misinterpreted হবে
# - Factory belt overload detect হবে না
# - Satellite signal drop হতে পারে
# - Game frame overheating হবে
# - Stock trade window miss হবে

# ✅ এই প্রবলেমটি ব্যবহার করে:
# - Circular system-এ performance hotspot খুঁজে বের করা যায়
# - AI optimization logic implement করা যায়
# - Automated prediction ও scheduling সিস্টেম বানানো যায়
