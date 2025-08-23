


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%(len(nums))
        
        # rotate_part=[nums[i] for i in range(len(nums)-k,len(nums))]
        
        # shift=len(nums)-k-1
        
        # while shift>=0:
        #     nums[shift+k]=nums[shift]
        #     shift-=1
        
        # for i in range(k):
        #     nums[i]=rotate_part[i]  
        
        
        ##Alternative way
        
        def reverse(start, end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                
                start+=1
                end-=1
                
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)
        
        
        
# ------------------------------
# Real-World Applications of Rotate Array
# ------------------------------

# 1. Buffer / Queue Management:
#    - Network routers বা streaming systems এ circular buffer ব্যবহার হয়।
#    - নতুন ডেটা এলে পুরোনো ডেটা shift করে জায়গা তৈরি করা হয়।

# 2. Round-Robin Scheduling:
#    - Operating System এর CPU time-slice allocation।
#    - Task বা worker list কে rotate করে scheduling করা হয়।
#    - Example: Workers A, B, C → next day rotation → B, C, A.

# 3. Image Processing / Graphics:
#    - Pixel shifting, scroll effects বা circular convolution করতে rotation ব্যবহার হয়।

# 4. Cryptography (Caesar Cipher):
#    - Letters কে rotate করে নতুন ciphertext বানানো হয়।
#    - Example: HELLO rotated by 3 → KHOOR.

# 5. Data Stream Analysis:
#    - Sensor readings IoT devices এ circular buffer এ রাখা হয়।
#    - নতুন মান এলে পুরোনো মান rotate করে shift হয়।

# 6. Playlist / Media Queue:
#    - Spotify/YouTube playlist এ গান শেষ হলে queue rotate হয়।
#    - পরের গান সামনে চলে আসে।

# 7. Gaming:
#    - Snake game বা board games (Monopoly, Ludo) এ player positions ঘোরাতে rotation ব্যবহার হয়।

# 8. Time/Calendar Systems:
#    - Clock এর hour hand ঘোরানো বা দিন-তারিখ হিসাব করার সময় circular rotation।
#    - Example: আজ বৃহস্পতিবার, 3 দিন পর → রবিবার।
