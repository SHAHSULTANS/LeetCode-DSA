class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # l=0
        # r=len(nums)-1

        def binary_search(l,r):
            # print("hello")
            if l>r:
                return -1
            mid=(l+r)//2
            # print(nums[mid])
            if nums[mid]==target:
                return mid

            if nums[mid]<target:
                return binary_search(mid+1,r)
            else:
                return binary_search(l,mid-1)


        return binary_search(0,len(nums)-1)

        # while l<=r:
        #     mid=(l+r)//2

        #     if nums[mid]==target:
        #         return mid

        #     if nums[mid]<target:
        #         l=mid+1
        #     else:
        #         r=mid-1

        # return -1
        
        
# ------------------------------
# Real-World Applications of Binary Search
# ------------------------------

# 1. Dictionary / Word Search:
#    - Digital dictionaries বা spell-checkers তে একটি শব্দ খুঁজতে।
#    - যেমন: Oxford Dictionary API বা auto-complete systems।

# 2. Database Indexing:
#    - Indexed database tables থেকে দ্রুত record খুঁজে বের করা।
#    - Example: SQL B-Tree indexing, file systems, key-value stores।

# 3. E-commerce / Price Search:
#    - Sorted price list থেকে নির্দিষ্ট মূল্য বা product খুঁজতে।
#    - Example: Amazon, eBay – price filter বা binary search for discounts।

# 4. Search in Large Datasets:
#    - Scientific data (weather, satellite, genomics) বা financial data।
#    - Example: Temperature readings, stock prices, sorted time-series data।

# 5. Gaming:
#    - Leaderboard থেকে player rank খুঁজতে।
#    - Example: Scoreboard sorted array → quickly find player position.

# 6. Software Tools:
#    - Auto-complete, code editors, search suggestions।
#    - Example: IDEs like VSCode, PyCharm → sorted list of function names।

# 7. Networking:
#    - IP routing table lookups, subnet searches।
#    - Example: Router lookup using sorted network prefixes.

# 8. Real-Time Systems:
#    - Sensor data processing, threshold detection।
#    - Example: IoT devices storing sorted readings → quickly detect target range.
