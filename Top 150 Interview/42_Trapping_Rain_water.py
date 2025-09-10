class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0

        stack=[]

        for i in range(len(height)):

            while stack and stack[-1][0]<=height[i]:
                # print("pop ",i, " ", stack[-1][0]-stack[-1][1])
                ans+=stack[-1][0]-stack[-1][1]
                stack.pop()


            if stack:
                stack.append((max(stack[-1][0],height[i]),height[i]))

            else:
                stack.append((height[i],height[i]))


        # print(stack)
        if stack:
            maximum=0
            while stack:
                last=stack.pop()
                maximum=max(last[1],maximum)
                ans+=(maximum-last[1])


        return ans




# ==============================
# Real-World Applications of Trapping Rain Water Problem
# ==============================

# 1. Urban Flood Management (শহরের জলাবদ্ধতা নিয়ন্ত্রণ)
#    শহরের রাস্তাঘাট বা কলোনিতে কোন নিচু জায়গায় বৃষ্টির পানি জমে যাবে 
#    তা simulation করে বের করতে এই অ্যালগরিদম ব্যবহার করা যায়।

# 2. Reservoir / Dam Design (ড্যাম ও জলাধার ডিজাইন)
#    পাহাড়ের ফাঁক বা উঁচু জায়গার মাঝে পানি কতটুকু জমবে, 
#    সেই হিসাব ড্যাম ইঞ্জিনিয়াররা এই লজিক দিয়ে বের করেন।

# 3. Agriculture & Irrigation (কৃষিক্ষেত্র ও সেচব্যবস্থা)
#    ক্ষেতের উঁচু-নিচু জায়গায় কোথায় পানি বেশি সময় ধরে থাকবে,
#    তা বুঝে ফসলের জন্য সেচের পরিকল্পনা করা হয়।

# 4. Computer Graphics / Game Development
#    গেম বা virtual world-এ বৃষ্টির পর পানি কোথায় জমবে
#    সেটা realistic effect দেখানোর জন্য এই অ্যালগরিদম ব্যবহার হয়।

# 5. Oil & Gas Reservoir Simulation
#    ভূগর্ভের উঁচু-নিচু শিলার মাঝে কোথায় তেল বা গ্যাস জমবে 
#    তা বের করতে একই ধরনের logic ব্যবহার করা হয়।
