class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        if l1+l2==len(s3):
            
            dp=[[False]*(l2+1) for _ in range(l1+1)]
            
            
            self.flag=False
            
            def dfs(i,j,k):
                if dp[i][j]==True:
                    return
                
                if i==l1 and j==l2:
                    self.flag=True
                    return

                dp[i][j] = True    
                if i<l1:
                    if s1[i]==s3[k]:
                        dfs(i+1,j,k+1)
                
                if j<l2:
                    if s2[j]==s3[k]:
                        dfs(i,j+1,k+1)
              

            dfs(0,0,0)
            return self.flag
                        
                                
        else:
            return False
        
        

# ----------------------------------------------------------------------------------

# ✅ এখন বাস্তব জীবন (Real Life) এ এই বিষয়টা কোথায় কাজে লাগে?

# 1. 🗣️ Speech Recognition — একাধিক বক্তার কথা চিনে ফেলা
# ধরো, দুইজন মানুষ (মাহিন আর রফিক) একসাথে কথা বলছে।

# একজন বলছে: hello how are you
# আরেকজন বলছে: hi I am fine
# পুরো রেকর্ডে আছে: hello hi how I are am you fine
# এখন AI বুঝবে কীভাবে কে কী বলেছে? 
# 👉 এই সমস্যাকে সমাধান করতে interleaving চেক করা হয়

# ✅ উপকার:
# বক্তাভেদে শব্দ আলাদা করা যায়, Speech-to-text অনেক বেশি accurate হয়

# ----------------------------------------------------------------------------------

# 2. 📄 Document Merge — Google Docs / Git
# তুমি ও তোমার বন্ধু একসাথে একটি ফাইল লিখছো
# তুমি লিখছো: "Intro: AI is useful"
# সে লিখছে: "Features: Fast, Smart"
# ফাইনাল ফাইল: Intro: Features: AI Fast, is Smart, useful

# 👉 এই অবস্থায় বোঝার দরকার, ফাইলটি দুইজনের লেখার একটি বৈধ মিশ্রণ কি না (interleaving)
# ✅ উপকার:
# ফাইল মিশ্রণে কে কী লিখেছে তা বোঝা সহজ হয়

# ----------------------------------------------------------------------------------

# 3. 💬 Messaging App / Chat Analysis
# দুইজন user একসাথে মেসেজ পাঠাচ্ছে।

# User A: hi, how r u
# User B: hello, I am good
# AI chatbot system যদি বুঝতে চায় কে কোন অংশ লিখেছে, তাহলে interleaving দরকার

# ✅ উপকার:
# Conversation tracking, toxic message filtering, auto-reply সব জায়গায় উপকার

# ----------------------------------------------------------------------------------

# 4. 🧬 DNA Sequencing / Genetic Recombination
# দুইটা DNA স্ট্র্যান্ড: মা এবং বাবার
# শিশুর DNA যদি তাদের interleaving হয়, তাহলে বুঝা যাবে mutation হয়নি

# ✅ উপকার:
# Genetic match, disease tracking, ancestry verification সম্ভব

# ----------------------------------------------------------------------------------

# 5. 💾 Database Transaction Interleaving
# দুইটি ব্যাংক ট্রান্স্যাকশন একই সময়ে চলছে:
# Transaction 1: deposit
# Transaction 2: withdraw
# Log ফাইল দেখছে: Start T1 → Start T2 → Deposit → Withdraw → End T1 → End T2

# 👉 Valid interleaving কিনা দেখে ডেটা corruption হয়েছে কিনা বোঝা যায়

# ✅ উপকার:
# Database concurrency control, system debugging

# ----------------------------------------------------------------------------------

# 6. 🎼 Music Composition — Layered Track Mixing
# Drum: D1 D2 D3
# Guitar: G1 G2 G3
# Final mixed: D1 G1 D2 G2 D3 G3 → valid interleaving?

# ✅ উপকার:
# AI music system ঠিকমতো beat ও instrument sync করতে পারে

# ----------------------------------------------------------------------------------