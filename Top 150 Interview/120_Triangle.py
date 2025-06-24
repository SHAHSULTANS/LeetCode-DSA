class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        r=len(triangle)
        
        dp=[[-1]*len(triangle[i]) for i in range(r)]
        # print(dp)
            
        
        def dfs(row,column_of_row):
            if row==r-1:
                return triangle[row][column_of_row]
            if dp[row][column_of_row]!=-1:
                return dp[row][column_of_row]
            
            left_total=triangle[row][column_of_row]+dfs(row+1,column_of_row)
            right_total=triangle[row][column_of_row]+dfs(row+1,column_of_row+1)
            
            dp[row][column_of_row]=min(left_total,right_total)
            return dp[row][column_of_row]
        

        return dfs(0,0)



# ✅ Application 1: Network Packet Routing
# প্রতিটি স্তরে একাধিক রাউটার এবং প্রতিটি রাউটার থেকে ২টি সম্ভাব্য পথ আছে।
# উদ্দেশ্য: সবচেয়ে কম latency-তে প্যাকেট পাঠানো।

# ✅ Application 2: Multi-stage Financial Planning
# বছরে বছরে বিনিয়োগ সিদ্ধান্ত নিতে হয় (Safe / Risky), প্রতিটি সিদ্ধান্তের রিটার্ন ভিন্ন।
# সর্বনিম্ন ঝুঁকিতে সর্বোচ্চ রিটার্ন অর্জন করতে এই প্যাটার্ন ব্যবহৃত হয়।

# ✅ Application 3: Robotics / Drone Navigation
# ড্রোন বা রোবট একাধিক স্তরভিত্তিক সিদ্ধান্ত নেয় — কোন পথে গেলে সবচেয়ে কম এনার্জি / ঝুঁকি।
# প্রতিটি স্তরে ২টি সম্ভাব্য মুভমেন্ট অপশন থাকে।

# ✅ Application 4: Layered Compression Techniques
# Progressive image বা video compression-এ প্রতিটি লেভেলে বিভিন্ন encoding অপশন থাকে।
# যেটি কম distortion বা size দেয়, সেটি বেছে নিতে এই প্যাটার্ন প্রয়োগ হয়।