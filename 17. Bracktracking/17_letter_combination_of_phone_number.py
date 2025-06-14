class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        
        ans=[]
        n=len(digits)
        if n==0:
            return ans
        
        def dfs(ar,index):
            if len(ar)==n:
                ans.append("".join(ar.copy()))
                return
            
            for i in range(index,n,1):
                letters_in_digit=keypad_dict[digits[i]]
                
                for char in letters_in_digit:
                    ar.append(char)
                    dfs(ar,i+1)
                    ar.pop()
                    
        dfs([],0)
        return ans            

# Problem 17: Letter Combinations of a Phone Number
# বাস্তব জীবনের প্রয়োগ (Real-world Applications) এবং প্রতিটির জন্য উদাহরণ:

# ১. ভ্যানিটি ফোন নাম্বার (Vanity Phone Numbers)
# কোম্পানিগুলো তাদের ফোন নাম্বারকে সহজে মনে রাখার মতো বানাতে চায়।
# যেমন: 1-800-FLOWERS → ইনপুট: 3569377 → সম্ভাব্য শব্দ: 'FLOWERS'

# ২. স্মার্ট কনট্যাক্ট সার্চ (Smart Contact Search)
# মোবাইলে যখন নাম খুঁজতে সংখ্যায় টাইপ করি, তখন সেটি সম্ভাব্য নাম সাজেস্ট করে।
# যেমন: ইনপুট '726' → সম্ভাব্য নাম: 'SAM', 'PAN', 'RAM'

# ৩. কাস্টমার সার্ভিস IVR রাউটিং
# কলার যখন কিপ্যাডে নির্দিষ্ট নাম্বার টাইপ করে, তখন তার ভিত্তিতে বিভাগ নির্বাচন হয়।
# যেমন: ইনপুট '4357' → শব্দ: 'HELP' → ইউজারকে সাহায্য বিভাগে পাঠানো হয়

# ৪. সিকিউরিটি ও পাসকোড জেনারেশন
# কিপ্যাড-ভিত্তিক পাসওয়ার্ড সিস্টেমে সংখ্যার থেকে সম্ভাব্য শব্দ বানিয়ে যাচাই করা হয়।
# যেমন: ইনপুট '7283' → সম্ভাব্য শব্দ: 'SAVE', 'RAVE', 'SATE' ইত্যাদি → সিস্টেম যাচাই করে

# ৫. টেক্সট প্রেডিকশন ও অটোকমপ্লিট (T9 Typing)
# পুরানো মোবাইলের মতো T9 টাইপিং সিস্টেমে দ্রুত টাইপ করার সুবিধা।
# যেমন: ইনপুট '4663' → সম্ভাব্য শব্দ: 'GOOD', 'HOME', 'GONE'

# এই সমস্যার মাধ্যমে ব্যাকট্র্যাকিং, রিকার্সন ও ইউজার ইন্টারফেস ডিজাইন শিখা যায়।
