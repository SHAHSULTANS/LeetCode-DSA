class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        
        def dfs(s,row,col):
            if row==n and col==n:
                ans.append(s)
                return
            
            
            #call opening bracket
            if row<n:
                dfs(s+"(",row+1,col)
             
            #call closing bracket 
            if col<n and col<row:
                dfs(s+")",row,col+1)   
                
        dfs("",0,0)
        return ans
                
                
# ✅ Real-World Applications of "22. Generate Parentheses"

# 🔸1. Compiler Design (Code Parsing):
# যখন একটি কম্পাইলার বা interpreter parentheses/check করে, যেমন:
#   - {}, [], (), nested structure ঠিক আছে কিনা
# তখন ব্যাকট্র্যাকিং বা এই ধরনের জেনারেশন দরকার হয়।

# 🔸2. Expression Generation:
# Calculator apps বা code formatting tools-এ সঠিকভাবে expression বানাতে গেলে 
# valid parentheses combination তৈরি করতে হয়।

# 🔸3. Math Equation Solvers:
# যেসব সফটওয়্যার অ্যালজেব্রিক এক্সপ্রেশন (যেমন: (a+b)*(c-d)) তৈরি বা সলভ করে, 
# সেসব জায়গায় valid parenthesis combinations খুব দরকার।

# 🔸4. Regex বা Pattern Matching Generator:
# কোনটা optional, group, repeated — এসব বোঝাতে regular expressions এ parentheses ব্যবহৃত হয়।
# সেগুলোর valid combination গুলো অটোমেটিক ally বানাতে এই algorithm দরকার।

# 🔸5. XML/HTML Tag Generator:
# যেখানে open-close ট্যাগ একে অপরকে match করতে হয় 
# যেমন `<div><p></p></div>` — এদের validate বা generate করার সময় এমন ব্যাকট্র্যাকিং লাগে।

# 🔸6. Code Formatting / Linter Tools:
# Parentheses এর ব্যালেন্স ঠিক আছে কিনা, সঠিকভাবে nest করা হয়েছে কিনা —
# এসব চেক করতে গিয়ে এই প্রবলেমের মতো ব্যাকট্র্যাকিং লাগে।

# 🔸7. Interview Question / Programming Challenge:
# এই প্রবলেম ব্যাকট্র্যাকিং শেখার জন্য ক্লাসিক উদাহরণ।
# মূলত tree structure-এ সব সম্ভাব্য valid path বের করা হয়।

# 🧠 Summary:
# এই প্রবলেম যেকোনো context-এ দরকার হয় যেখানে —
#   → balanced open-close structure দরকার
#   → এবং তাদের সব valid combination generate করতে হয়
