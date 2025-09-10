class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_here=min_here=nums[0]
        ans=nums[0]

        for i in range(1,len(nums)):
            prev_max = max_here
            prev_min = min_here

            max_here = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            # print(max_here)
            min_here = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            ans=max(ans,max_here)
            # print(ans)

        return ans
    
# Applications of "Maximum Product Subarray" (LeetCode 152)
#
# 1. Stock Market Analysis:
#    - প্রতিদিনের লাভ/ক্ষতির factor (positive/negative) দেওয়া থাকলে
#      কোন একটানা সময় invest করলে টাকা সবচেয়ে বেশি বাড়বে সেটা বের করা যায়।
#
# 2. Signal Processing:
#    - একটানা সময়ের মধ্যে signal strength multiply হয়ে কোথায় সবচেয়ে শক্তিশালী signal হয় তা detect করা।
#
# 3. Biology / Genomics:
#    - DNA বা protein sequence alignment এ একটানা region এর "match" (+ve) আর "mismatch" (-ve) স্কোর থেকে
#      সবচেয়ে strong alignment segment বের করা।
#
# 4. Computer Graphics:
#    - Pixel brightness বা contrast multiplier দিয়ে কোন continuous region এ সবচেয়ে বেশি effect পড়ছে তা খুঁজে বের করা।
#
# 5. Gaming / Score Combos:
#    - গেমে একটানা actions (bonus = positive, penalty = negative) এর মধ্যে কোন continuous combo
#      player কে সবচেয়ে বড় multiplier দিচ্ছে সেটা বের করা।
