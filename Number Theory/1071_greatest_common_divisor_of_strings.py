class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        l1=len(str1)
        l2=len(str2)
        length_pefix=l2
        
        while length_pefix:
            first=False
            second=False
            prefix=str2[0:length_pefix]
            # print(prefix)
            s=""
            while l1>len(s) or l2>len(s):
                s+=prefix
                if s==str1:
                    first=True
                # print(s," ",str1," ->",(s==str1))
                if s==str2:
                    second=True
                    
            if first and second:
                return prefix
            
            length_pefix-=1
            
        return ""
    
    
# 📌 Applications of 1071. Greatest Common Divisor of Strings

# ✅ 1. Communication Protocol Optimization
# যখন দুটি ডিভাইস একে অপরকে বারবার একই মেসেজ পাঠায় (যেমন: "ACKACKACK", "ACKACK")
# তখন GCD string ("ACK") বের করে pattern identify করা যায় → bandwidth optimize হয়।

# ✅ 2. Log File Pattern Detection
# সার্ভার লগে যদি একই message বারবার আসে, যেমন: "ERROR404ERROR404"
# তাহলে GCD string বের করে বুঝা যায় কোন error pattern বারবার হচ্ছে।

# ✅ 3. DNA Sequence Pattern Matching
# Bioinformatics-এ GCD string ব্যবহার হয় repeat হওয়া gene-segment খুঁজতে,
# যেমন: "ACGTACGTACGT" এবং "ACGTACGT" → GCD = "ACGT"

# ✅ 4. Music Pattern Recognition
# AI-Generated Music system-এ common rhythm বা loop detect করার জন্য GCD string বের করা হয়,
# যেমন: "DOREMEFAREMEFA" & "DOREMEFA" → "DOREMEFA"

# ✅ 5. Document or Email Template Deduplication
# Auto-generated message বা email যদি একই structure follow করে,
# তাহলে GCD string বের করে template detect করা যায়।
# যেমন: "HelloUserWelcomeHelloUserWelcome" → GCD = "HelloUserWelcome"

# ✅ 6. Natural Language Processing (NLP)
# Repeating phrase, slogan বা subtitle detect করার কাজে GCD of strings ব্যবহৃত হয়।

# ✅ 7. File Compression Algorithms
# Repeating structure detect করে redundancy minimize করতে GCD of strings গুরুত্বপূর্ণ ভূমিকা রাখে।

# 🔁 Summary:
# যেকোনো জায়গায় যেখানে string repetition বা pattern থাকে (log, DNA, communication, document, music),
# সেখানে এই সমস্যা বাস্তবে ব্যবহৃত হয়।
