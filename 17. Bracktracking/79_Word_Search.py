class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        
        visited=[[False]*col for _ in range(row)]
        self.ans=False
        
        
        def dfs(i,j,ctn):
            if ctn==len(word):
                self.ans=True
                return
                
            # Left move
            if j-1 >= 0 and board[i][j-1] == word[ctn] and not visited[i][j-1]:
                visited[i][j-1] = True
                # ar.append(word[ctn])
                dfs( i, j-1, ctn + 1)
                visited[i][j-1] = False
                # ar.pop()
                
            #right move
            if j+1<col and board[i][j+1] == word[ctn] and not visited[i][j+1]:
                visited[i][j+1] = True
                # ar.append(word[ctn])
                dfs( i, j+1, ctn + 1)
                visited[i][j+1] = False
                # ar.pop()
            
            
            #up move
            
            if i-1>= 0 and board[i-1][j] == word[ctn] and not visited[i-1][j]:
                visited[i-1][j] = True
                # ar.append(word[ctn])
                dfs( i-1, j, ctn + 1)
                visited[i-1][j] = False
                # ar.pop()
                
            #down move
            if i+1<row and board[i+1][j] == word[ctn] and not visited[i+1][j]:
                visited[i+1][j] = True
                # ar.append(word[ctn])
                dfs( i+1, j, ctn + 1)
                visited[i+1][j] = False
                # ar.pop()
        
        
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    visited[i][j]=True
                    dfs(i,j,1)
                    visited[i][j]=False
                    
                    
        return self.ans
        
        
        
# ✅ Word Search (Matrix-based DFS) সমস্যার রিয়েল ওয়ার্ল্ড অ্যাপ্লিকেশনসমূহ (বাংলায়):

# ১. Text Recognition in Images (OCR):
#    স্ক্যান করা বই/ডকুমেন্ট থেকে অক্ষর বা শব্দ শনাক্ত করতে গ্রিড বা ম্যাট্রিক্সে DFS ব্যবহার করা হয়।

# ২. Crossword Puzzle Solver:
#    শব্দ খোঁজার জন্য গ্রিডে বিভিন্ন দিক ঘেঁটে (up/down/left/right) DFS দিয়ে চেক করা হয়।

# ৩. Spell Checker in Word Processors:
#    গ্রিড-ভিত্তিক কীবোর্ড (যেমন: ফোন কীবোর্ড) থেকে ভুল টাইপ করা শব্দ সঠিকভাবে খুঁজে বের করতে এই এলগরিদম ব্যবহার হয়।

# ৪. Touch-screen Input Prediction:
#    যদি ইউজার ভুলভাবে বাটন টাচ করে, তবে নিকটবর্তী বাটনগুলো থেকে সম্ভাব্য শব্দ খোঁজা হয় (গ্রিড traversal দিয়ে)।

# ৫. AI in Word Games (e.g., Boggle):
#    বোগল বা শব্দ খোঁজা গেমে কম্পিউটার শব্দ খুঁজে বের করার জন্য matrix traversal + DFS ইউজ করে।

# ৬. DNA Sequence Pattern Matching:
#    DNA nucleotide গ্রিডে নির্দিষ্ট প্যাটার্ন বা সিকোয়েন্স খোঁজার সময় এমন DFS-based পদ্ধতি কাজে লাগে।

# ৭. Mobile Keypad Typing Suggestion:
#    একাধিক বাটনের সম্ভাব্য কম্বিনেশন থেকে শব্দ খুঁজে বের করতে ম্যাট্রিক্স traversal দরকার হয়।

# ৮. Hidden Word Finder in Educational Games:
#    শিশুদের জন্য বানানো শব্দ-শেখার গেমে গ্রিড থেকে নির্দিষ্ট শব্দ খুঁজে বের করতে DFS ব্যবহৃত হয়।

# 🔁 সংক্ষেপে: Word Search সমস্যা মূলত দুই-মাত্রিক ডেটা থেকে প্যাটার্ন খোঁজার ক্ষেত্রে ব্যবহার হয়, যেখানে চরিত্রগুলো সংলগ্ন অবস্থায় থাকে।
