class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydic={}
        
        for item in nums:
            if mydic.get(item):
                mydic[item]+=1
            else:
                mydic[item]=1
                
        frequent_arr=[]
        for key in mydic:
            value=mydic[key]
            frequent_arr.append((value,key))
            
        frequent_arr.sort(reverse=True)
        
        ans=[]
        i=0
        while k:
            ans.append(frequent_arr[i][1])
            i+=1
            k-=1
        
        return ans
    
# ✅ Real-World Applications of Top K Frequent Elements
# Along with ❌ What happens without it

# 1. 📊 Search Engine (Google, YouTube, Bing)
# - Input: ["python", "ai", "ai", "music"]
# - Output: Top searched keywords → ["ai", "python"]
# ✅ Use: Show trending searches, personalized suggestions
# ❌ Without it: No way to show what's popular → poor user engagement

# 2. 🛒 E-commerce (Amazon, Daraz, Flipkart)
# - Input: ["phone", "laptop", "phone"]
# - Output: Best selling products → ["phone"]
# ✅ Use: Display "Top Selling", recommend hot deals
# ❌ Without it: Customer can't discover popular products → lower sales

# 3. 🤖 AI Chatbot (Customer support bots)
# - Input: ["reset_password", "login_issue", "reset_password"]
# - Output: Most common user intent → ["reset_password"]
# ✅ Use: Improve training for popular intents, faster replies
# ❌ Without it: Bot wastes time on less important issues → frustrates users

# 4. 🧾 Error Logs (DevOps, Server Monitoring)
# - Input: ["502", "404", "502"]
# - Output: Top error → ["502"]
# ✅ Use: Dev team prioritizes fixing the most frequent issue
# ❌ Without it: Random bug fixing, critical errors stay unresolved

# 5. 📱 Social Media (Twitter, Instagram, TikTok)
# - Input: ["#ai", "#fun", "#ai"]
# - Output: Trending hashtags → ["#ai"]
# ✅ Use: Show current trends, engage users with hot topics
# ❌ Without it: Trends feel irrelevant or outdated → less interaction

# 6. 🔐 Security Logs (Firewall, Intrusion Detection)
# - Input: ["10.0.0.1", "10.0.0.1", "10.0.0.2"]
# - Output: Suspicious IP → ["10.0.0.1"]
# ✅ Use: Block IPs that hit server repeatedly, stop brute-force attacks
# ❌ Without it: Hackers go unnoticed → system becomes vulnerable

# 7. 📚 Education Analytics (Online Learning Platforms)
# - Input: ["dp", "binary tree", "dp"]
# - Output: Most asked topic → ["dp"]
# ✅ Use: Focus content, coaching, or videos on popular weak topics
# ❌ Without it: Teachers waste time on less-needed content → poor student results
