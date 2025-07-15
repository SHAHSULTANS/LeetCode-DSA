class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        ans=[1 for _ in range(n)]
        
        for i in range(1,n,1):
            if ratings[i]>ratings[i-1]:
                ans[i]=ans[i-1]+1
                
        i=n-2
        while i>=0:
            if ratings[i]>ratings[i+1]:
                ratings[i]=max(ratings[i],ratings[i+1]+1)
                
        return sum(ans)
    
# 📌 Leetcode 135: Candy Problem

# ✅ Real-World Applications

# 1. 🏢 Bonus Distribution
# - Employees rated: [2, 4, 3, 5]
# - More rating → More bonus than neighbors

# 2. 🎓 Grading/Scholarship
# - Students' score = [78, 82, 80]
# - Better mark → Higher grade/scholarship than adjacent

# 3. 👷 Resource Allocation
# - Workers with efficiency = [3, 5, 2]
# - More efficient → More tools given

# 4. 🧠 AI Reward System
# - Learner score = [1, 2, 2]
# - Reward tier increases for better performer

# 5. 🏥 Hospital ICU Prioritization
# - Patient critical score = [2, 3, 5]
# - More critical → More medical attention

# ❌ Without this algorithm:
# - Unfair distribution
# - Wrong people rewarded
# - Trust issue in system
# - Efficiency wasted
