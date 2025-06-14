class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #3x3 grid check exists duplicate or not
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                if self.small_grid_check_duplicate(i,j,board):
                    # print(i,j)
                    return False
        
        
        
        #Each row check 
        for i in range(9):
            mydic={}
            for j in range(9):
                if mydic.get(board[i][j]):
                    return False
                if board[i][j]!="" and board[i][j]!=".":
                    mydic[board[i][j]]=1
                    
        #Each Column Check    
        
        for i in range(9):
            mydic={}
            for j in range(9):
                if mydic.get(board[j][i]):
                    return False
                if board[j][i]!="" and board[j][i]!=".":
                    mydic[board[j][i]]=1        
                    
        return True
    
    
    
    def small_grid_check_duplicate(self,row,col,board):
        mydic={}
        
        for i in range(row,row+3,1):
            for j in range(col,col+3,1):
                if mydic.get(board[i][j]):
                    # print(i,j)
                    return True
                if board[i][j]!="" and board[i][j]!=".":
                    mydic[board[i][j]]=1

                # print(mydic)
                
        return False
    
    
    
    
# ✅ Real-World Applications of "36. Valid Sudoku"

# 🔸1. Data Validation in Grids/Spreadsheets:
#    যেমন কোনো ওয়েব অ্যাপে ইউজার যদি ৯×৯ কোষের ডেটা ইনপুট করে,
#    সেখানেও প্রতি রো ও কলামে duplicate থাকা মানে ভুল ডেটা।
#    Valid Sudoku এর মতো লজিক ব্যবহার করে ফর্ম সাবমিশনের আগে ভ্যালিডেশন করা যায়।

# 🔸2. Constraint Checking in Scheduling Systems:
#    ধরো স্কুলের টিউশন সেন্টারে ক্লাস রুম-সিডিউল তৈরি করো,
#    যেখানে একই ঘন্টার মধ্যে কোনো শিক্ষক বা রুম দুইবার ব্যবহৃত হবে না।
#    Sudoku এর row, column, 3×3 বক্স চেক করার লজিক এখানে কাজে লাগে।

# 🔸3. Database Uniqueness Enforcement:
#    কোনো টেবিলে composite key যেমন (country, state, city) ইউনিক কিনা চেক করার সময়,
#    ২ডি ম্যাট্রিক্স পরিষ্করণ ও ইউনিকিটি নিশ্চিত করার Sudoku-র ন্যায় পদ্ধতি ব্যবহার হয়।

# 🔸4. Memory/Grid Integrity in Embedded Systems:
#    কিছু এম্বেডেড ডিভাইসে RAM-এ data blocks ৯×৯ গ্রিডের মতো বসানো থাকে,
#    ডেটা কেউ ওভারল্যাপ করে লেখেনি তা চেক করার জন্য Sudoku-style integrity check দরকার হতে পারে।

# 🔸5. Game Development Engines:
#    UI-ত বা খেলার লেভেল ডিজাইনে ২ডি গ্রিডে কোনো অবৈধ অবজেক্ট কনফিগার করা হয়নি
#    তা নিশ্চিত করতে Similar validation logic প্রয়োগ করা যায়।

# 🔸6. Machine Learning Data Preprocessing:
#    যদি কোনো ML মডেলে ইনপুট হিসেবে ৯×৯ বা N×N ম্যাট্রিক্স আসে,
#    যেখানে প্রতিটি রো, কলাম বা সাবগ্রিডে বিশেষ নিয়ম মানতে হবে,
#    তাহলে Valid Sudoku problem এর সমাধান মডেল হিসেবে কাজে আসে।

# 🔸7. Configuration File Validation:
#    কিছু সিস্টেমে settings/configuration matrix আকারে থাকে,
#    প্রতিটি খানে বাদ্য, রং, বা প্যারামিটার নির্দিষ্ট হওয়া উচিত।
#    ভ্যালিড সুডোকু চেক করে নিশ্চিত করা যায় কোনো ক্ষেত্র পুনরাবৃত্তি হয়নি।

# 🧠 সার সংক্ষেপ:
#  “Valid Sudoku” মানে একটি ২ডি গ্রিডে প্রতিটি রো, কলাম ও নির্দিষ্ট सब–বক্সে কপিকলন বা
#   ডুপ্লিকেশন নেই—এই ধারণা প্রয়োগ করা যায় যেখানেই ২ডি ডেটা ইউনিক ও constraint-based।
