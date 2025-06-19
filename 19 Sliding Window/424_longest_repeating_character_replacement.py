class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=1
        maximum=0
        mydic={}
        left_pointer=0
        
        for index,char in enumerate(s):
            if char in mydic:
                mydic[char] += 1
            else:
                mydic[char] = 1
            
            maximum=max(mydic[char],maximum)
            summation=sum([mydic[key] for key in mydic])
            
            #MAIN LOGIC
            if summation-maximum<=k:
                ans=max(ans,index-left_pointer+1)
            else:
                while True:
                    mydic[s[left_pointer]]-=1
                    left_pointer+=1
                    
                    summation = sum(mydic.values())

                    # Calculate the maximum value among dictionary values
                    maximum = max(mydic.values()) if mydic else 0
                    
                    if summation-maximum<=k:
                        ans=max(ans,index-left_pointer+1)
                        break

                    
                
        return ans
    
    
# -------------------------------
# 📌 বাস্তব জীবনের অ্যাপ্লিকেশনসমূহ
# -------------------------------

# ১. টাইপিং কনসিস্টেন্সি বিশ্লেষণ:
#    একজন ব্যবহারকারী কতক্ষণ ধরে একই ক্যারেক্টার টাইপ করেছেন, 
#    তা নির্ণয় করতে ব্যবহৃত হয়, এমনকি মাঝে ১-২টি ভুল সহ্য করেও।

# ২. ইমেজ প্রসেসিং ও সিগন্যাল স্মুথিং:
#    একটি noisy কালার সিকোয়েন্সে সর্বোচ্চ k টি পিক্সেল বদলে 
#    সবচেয়ে বড় uniform (একই রঙ) ব্লক খুঁজে বের করা হয়।

# ৩. ইমোশনাল প্যাটার্ন ডিটেকশন (NLP):
#    টেক্সটে রিপিটেড আবেগ (যেমন 'sad sad happy sad') বিশ্লেষণ করে 
#    সীমিত শব্দ পরিবর্তন করে সবচেয়ে বড় consistent প্যাটার্ন বের করা।

# ৪. ভিডিও/সিগন্যাল error correction:
#    ভিডিও বা সিগন্যালের ডেটায় ছোটখাটো ত্রুটি উপেক্ষা করে 
#    বড় একরকম ব্লক সনাক্ত করার জন্য ব্যবহৃত হয়।

# ৫. ফরম্যাটিং কনফর্মিটি চেক:
#    বড় কোনো টেক্সট বা ডেটাতে নির্দিষ্ট ক্যারেক্টার (যেমন স্পেস, ট্যাব) 
#    কনসিস্টেন্টলি ব্যবহৃত হয়েছে কিনা, তা যাচাই করতে ব্যবহার করা যায়।

# -------------------------------
