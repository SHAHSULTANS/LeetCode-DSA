class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabets="abcdefghijklmnopqrstuvwxyz0123456789"

        newstring=[]
        for char in s:
            if char.lower() in alphabets:
                newstring.append(char.lower())
        # print("0".lower())
        # print(newstring)
        newstring="".join(newstring)
        return newstring==newstring[::-1]



class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True



# বাস্তব জীবনের অ্যাপ্লিকেশন (Real World Applications):
# 1. Search Engines (SEO) → সার্চ কিওয়ারি পালিনড্রোম হলে স্পেশাল সাজেশন/ফান ফ্যাক্ট দেখানো
# 2. Cybersecurity → পাসওয়ার্ড পালিনড্রোম হলে সেটা দুর্বল বলে গণ্য করা
# 3. Bioinformatics → DNA সিকোয়েন্স বিশ্লেষণে পালিনড্রোম সাইট খুঁজে বের করা (যেমন: EcoRI enzyme কাটিং সাইট "GAATTC")
# 4. Data Compression → পালিনড্রোম প্যাটার্ন ব্যবহার করে ডাটা কম জায়গায় রাখা
# 5. Messaging Apps → ইউজার যদি পালিনড্রোম টাইপ করে তবে মজার রিপ্লাই/ফিচার দেখানো
# 6. Natural Language Processing (NLP) → সাহিত্য, ব্র্যান্ড নাম, স্লোগান ইত্যাদিতে পালিনড্রোম চিহ্নিত করা