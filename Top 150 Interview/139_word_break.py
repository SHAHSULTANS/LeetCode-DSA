class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        self.ans=False
        dp=[False for _ in range(len(s))]
        
        def dfs(i):
            if i==len(s):
                self.ans=True
                return
            
            if dp[i]==True:
                return
            
            dp[i]=True
            # print("Yes calling")    
            for word in wordDict:
                if self.ans==False and s.startswith(word, i):
                    # print(s.find(word)," i ",i)
                    dfs(i+len(word))
                    
        dfs(0)
        return self.ans
                
                
# 📌 Leetcode 139: Word Break Problem
# ✅ Real-World Applications (with real examples)

# 1️⃣ 📱 Mobile Keyboard Suggestion / Autocorrect
# Input: "iamlearningai"
# wordDict = ["i", "am", "learning", "ai"]
# → System uses word break to suggest: "I am learning AI"
# ✅ Without it, keyboard couldn't suggest correct sentence

# 2️⃣ 🖨️ OCR (Optical Character Recognition)
# Extracted text: "welcometobangladesh"
# wordDict = ["welcome", "to", "bangladesh"]
# → Breaks into: "welcome to bangladesh"
# ✅ OCR can now show meaningful output, else it’s gibberish

# 3️⃣ 🔐 Password Security Check
# Password: "admin123"
# wordDict = ["admin", "password", "root"]
# → Breaks into ["admin"] + digits → weak password → reject
# ✅ Without word break, system couldn't detect dictionary words

# 4️⃣ 🧠 NLP Tokenization in Asian Languages
# Input: "我喜欢学习人工智能" (no spaces)
# wordDict = ["我", "喜欢", "学习", "人工智能"]
# → Breaks into valid tokens for AI to understand
# ✅ Used in translation, chatbots, and AI models

# 5️⃣ 🧾 Grammar Checking Tools
# Input: "thisisnotright"
# wordDict = ["this", "is", "not", "right"]
# → Valid sentence → Apply grammar rules
# ✅ Without break, system can't parse or correct the sentence

# 6️⃣ 🔎 Search Engine Query Breakdown
# Query: "topmobileunder15000"
# wordDict = ["top", "mobile", "under", "15000"]
# → Helps show relevant product results
# ✅ Otherwise search engine shows wrong/no result

# ✅ Summary:
# Word break algorithms help systems understand, validate, and
# process human inputs by breaking them into known/valid words.

            