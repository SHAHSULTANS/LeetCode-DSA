class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # উপরের সারি ও নিচের সারি ইনডেক্স (row)
        # Top and bottom row indices
        r1 = 0
        r2 = len(matrix) - 1

        # বাঁ পাশে ও ডান পাশে ইনডেক্স (column)
        # Left and right column indices
        c1 = 0
        c2 = len(matrix[0]) - 1

        # প্রতিটি outer layer ঘোরাতে যতক্ষণ পর্যন্ত ভেতরের দিকে যাচ্ছি
        # Process each outer layer, moving inward
        while r1 <= r2:

            # প্রতিটি স্কয়ার ব্লকে কতবার চারটি দিক ঘোরাতে হবে
            # How many steps to rotate in the current square layer
            loop = r2 - r1  
            updown = leftright = 0  # প্রতি চক্রে উপরে/নিচে ও বামে/ডানে যাওয়ার জন্য offset
                                    # Offsets to move up/down and left/right within the layer

            while loop:
                # চারটি প্রান্তের মান নাও
                # Get the values at four corners
                bottom_left = matrix[r2 - updown][c1]
                top_left = matrix[r1][c1 + leftright]
                top_right = matrix[r1 + updown][c2]
                bottom_right = matrix[r2][c2 - leftright]

                # চারটি প্রান্তের মান ঘোরাও (90° clockwise)
                # Rotate the corners 90 degrees clockwise
                matrix[r1][c1 + leftright] = bottom_left         # top-left = bottom-left
                matrix[r1 + updown][c2] = top_left              # top-right = top-left
                matrix[r2][c2 - leftright] = top_right          # bottom-right = top-right
                matrix[r2 - updown][c1] = bottom_right          # bottom-left = bottom-right

                # পরবর্তী পদক্ষেপে যাও (এক ধাপ বামে/ডানে ও উপরে/নিচে)
                # Move to next set of corners in the current layer
                loop -= 1
                leftright += 1
                updown += 1

            # এক লেয়ার ঘোরানোর পর ভেতরের পরবর্তী স্কয়ারে যাও
            # Move inward to the next inner layer
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1



# বাস্তব জীবনে কোথায় এই matrix (image) rotate ব্যবহার হয়:

# 1. 🖼️ ছবি সম্পাদনা সফটওয়্যার (Photo Editor):
#     - যখন ইউজার 'Rotate Right' বা 'Rotate Left' বোতামে ক্লিক করে,
#         তখন ছবির পিক্সেল গুলো 2D ম্যাট্রিক্স হিসেবে ঘোরানো হয়।

# 2. 🤖 মেশিন লার্নিং এবং কম্পিউটার ভিশন:
#     - ডেটা অগমেন্টেশনের জন্য ছবি ঘোরানো হয় যাতে মডেল বিভিন্ন কোণ থেকেও 
#         অবজেক্ট চিনতে পারে। উদাহরণ: হ্যান্ডরাইটিং রিকগনিশন।

# 3. 🎮 গেম ডেভেলপমেন্ট (2D গেম):
#     - Tetris-এর মত গেমে প্রতিটি ব্লক ঘোরানোর জন্য এই ম্যাট্রিক্স রোটেশন ব্যবহার হয়।

# 4. 🛰️ স্যাটেলাইট ইমেজ প্রসেসিং:
#     - স্যাটেলাইট বা ড্রোন থেকে পাওয়া ছবির অরিয়েন্টেশন ঠিক করার জন্য ঘোরানো হয়।

# 5. 📊 গ্রাফিকাল ইউজার ইন্টারফেস (GUI):
#     - যখন ইউজার কোন ছবি ঘোরাতে চায় GUI তে, তখন এটি কোড লেভেলে এমন ঘূর্ণন হিসেবেই ঘটে।

# Note: এখানে কোডে 90 ডিগ্রি clockwise ঘোরানো হচ্ছে image matrix।