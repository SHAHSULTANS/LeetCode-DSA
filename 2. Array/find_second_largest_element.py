


nums=[0,5,6]


first=second=float("-inf")

for num in nums:
    if num>first:
        second=first
        first=num
        
    if second<num<first:
        second=num
        
        
        
#sorted way

nums=list(set(nums))
nums.sort(reverse=True)

if len(nums)>1:
    second=nums[1]
else:
    print("NOne")        
    
        


# ------------------------------
# Real-World Applications of "Second Largest Element" Problem
# ------------------------------

# 1. Sports / Competitions:
#    - প্রতিযোগিতায় runner-up বের করতে (2nd highest score, 2nd fastest time)।
#    - Example: ক্রিকেট ম্যাচে second highest run scorer কে বের করা।

# 2. Business / Sales Analytics:
#    - কোন প্রোডাক্ট সবচেয়ে বেশি বিক্রি হয়েছে আর তারপরে কোনটা (second best seller)।
#    - Decision making: যদি top seller out-of-stock হয়, তাহলে next best কে প্রোমোট করা।

# 3. Hiring / Exams:
#    - চাকরির পরীক্ষায় বা কলেজ ভর্তি পরীক্ষায় second highest scorer কে বের করা।
#    - Tie-breaker বা scholarship eligibility check করতে কাজে লাগে।

# 4. Gaming Leaderboard:
#    - Online games এ 1st এবং 2nd rank খুঁজে বের করতে।
#    - Example: PUBG, FreeFire leaderboard – second top player কে highlight করা।

# 5. Stock Market / Finance:
#    - শেয়ার মার্কেটে সবচেয়ে বেশি বাড়া স্টক আর দ্বিতীয় বেশি বাড়া স্টক।
#    - Portfolio diversification এ সাহায্য করে।

# 6. Sensor Data / IoT:
#    - যদি একাধিক সেন্সর থাকে, তাহলে 2nd highest reading detect করা।
#    - Example: Temperature sensors – একটা সেন্সর faulty হলে second highest নিতে হবে।

# 7. Disaster Management:
#    - Flood level, earthquake magnitude, rainfall data – দ্বিতীয় সর্বোচ্চ মান নির্ণয়।
#    - First highest হলে অনেক সময় extreme outlier হয়, তাই second highest বেশি নির্ভরযোগ্য।

# 8. Sports Analytics:
#    - Player performance এ second best metrics খুঁজে বের করা।
#    - Example: একজন খেলোয়াড়ের second fastest century বা second highest wickets।
