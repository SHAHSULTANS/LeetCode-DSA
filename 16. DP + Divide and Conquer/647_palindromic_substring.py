class Solution:
    def countSubstrings(self, s: str) -> int:
        # unique={}
        n=len(s)
        total=n
        for center in range(n):
            # unique[s[center]]=1
            #odd len palindrome
            i=center-1
            j=center+1
            while i>=0 and j<n and s[i]==s[j]:
                # unique[s[i:j+1]]=1
                total+=1
                i-=1
                j+=1

            #even len palindrome:
            i=center
            j=center+1   

            while i>=0 and j<n and s[i]==s[j]:
                # unique[s[i:j+1]]=1
                total+=1
                i-=1
                j+=1

        return total


# Application example 1: Bioinformatics
# DNA/RNA sequence analysis-এ প্যালিনড্রোমিক সিকোয়েন্স খুঁজে এনজাইম recognition ও gene analysis করা হয়।

# Application example 2: Data Compression
# ডাটা কম্প্রেশনে রিপিটিশন pattern চিনে সেটা কমিয়ে স্টোরেজ সেভ করা হয়, 
# যেখানে প্যালিনড্রোমিক সাবস্ট্রিং খুঁজে তা কাজে লাগে।

# Application example 3: Natural Language Processing (NLP)
# ভাষায় রিদম বা বিশেষ প্যাটার্ন শনাক্ত করতে প্যালিনড্রোমিক সাবস্ট্রিং বিশ্লেষণ করা হয়,
# যেমন কবিতা বা শব্দের পুনরাবৃত্তি ধরার কাজে।

# Application example 4: Database Optimization
# বড় ডাটাবেসে ডুপ্লিকেট বা symmetric প্যাটার্ন শনাক্ত করে ডাটা ক্লিনিং ও সার্চ অপটিমাইজেশনে ব্যবহার হয়।
