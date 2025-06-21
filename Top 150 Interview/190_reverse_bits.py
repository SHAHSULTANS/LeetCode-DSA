class Solution:
    def reverseBits(self, n: int) -> int:
        bitar=[]

        def int_to_binary(n):
            if n==0:
                return

            int_to_binary(int(n/2))
            bitar.append(n%2)

        int_to_binary(n)
        bitar.reverse()
        while len(bitar)<32:
            bitar.append(0)
        s="".join(str(x) for x in bitar)
        # print(s)
        sum=0
        for index,bit in enumerate(bitar):
            if bit=='1':
                sum+=pow(2,(31-index))
                
        return sum
        
        # return  964176192
        
        
# ✅ বাস্তব জীবনে কোথায় কোথায় bit reversal দরকার হতে পারে:

    # 🛰️ 1. Network protocols:
    # কিছু communication protocol (যেমন Zigbee, Ethernet) এর মধ্যে 
    # bit ordering আলাদা হয়। তাই এক প্রটোকল থেকে আরেকটিতে ডেটা পাঠাতে
    # bit reversal দরকার হয়।

    # 🎮 2. Game graphics rendering:
    # পুরনো NES/retro গেমগুলোতে sprite data bit-reversed format এ থাকে।
    # এগুলো সঠিকভাবে draw করতে প্রতিটি byte বা 32-bit value উল্টে নিতে হয়।

    # 🧮 3. FFT (Fast Fourier Transform):
    # কিছু FFT অ্যালগরিদমে input index গুলোকে bit-reversed order এ রাখতে হয়
    # পারফরমেন্স বাড়ানোর জন্য।

    # 🛡️ 4. Cryptography বা Data compression:
    # Custom encryption বা কম্প্রেশন স্কিমে bit level manipulation দরকার হয়,
    # সেখানে অনেক সময় reverse bits প্রয়োজন হয়।

    # 📺 5. Embedded systems:
    # কিছু মাইক্রোকন্ট্রোলার বা ডিসপ্লে ডিভাইসে ডেটা রেজিস্টারে 
    # উল্টো বিট অর্ডারে পাঠাতে হয়।