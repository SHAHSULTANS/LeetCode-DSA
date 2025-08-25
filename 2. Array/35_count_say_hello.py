class Solution:
    def countAndSay(self, n: int) -> str:
        
        rle=[1]

        for i in range(1,n):
            newar=[]
            j=0
            while j<len(rle):
                ctn=1
                while j+1<len(rle) and rle[j]==rle[j+1]:
                    ctn+=1
                    j+=1
                
                # print(ctn)
                newar.append(ctn)
                newar.append(rle[j])
                j+=1
            rle=newar

        # print(rle)
        return ("".join(str(x) for x in rle))
            # print(newar)

                

                
# Count-and-Say (RLE) – Real World Applications

# 1. Data Compression
# --------------------
# Count-and-Say মূলত একটি Run-Length Encoding (RLE) sequence.
# RLE compresses repeated consecutive data.
# Example: In image processing, consecutive pixels of same color
# can be stored as (count, value) instead of storing every pixel.
# This reduces memory usage in black-and-white images or simple graphics.

# 2. DNA Sequence Analysis
# -------------------------
# In genomics, DNA has repeated nucleotides, e.g., "AAACCGGGTT".
# Count-and-Say or RLE can compress these sequences:
# "3A2C3G2T".
# Useful for storage, transmission, or pattern detection in DNA data.

# 3. Signal Processing
# --------------------
# In telemetry or sensor data, repeated identical readings may occur.
# Using RLE, repeated readings can be encoded as count + value,
# reducing storage or bandwidth, while preserving the sequence information.

# 4. Text or Log Compression
# ---------------------------
# Log files or large text files often have repeated characters or patterns.
# Count-and-Say encoding can compress sequences like:
# "aaaaabbbcc" → "5a3b2c"
# Useful in storage systems, log analysis, or telemetry data transfer.

# 5. Pattern Recognition
# ----------------------
# Count-and-Say sequences can be used to identify repetitive patterns
# in any sequential data: network packets, financial transactions,
# or repeated actions in online gaming.
# Example: Detecting repeated actions that indicate bots or fraud.

# 6. Teaching / Algorithm Visualization
# -------------------------------------
# Count-and-Say is used in computer science education
# to teach recursion, iterative sequence generation,
# and run-length encoding techniques.
