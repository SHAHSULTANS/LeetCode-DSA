import random


class RandomizedSet:

    def __init__(self):
        self.value_index={}
        self.key=[]

    def insert(self, val: int) -> bool:
        if val in self.value_index:
            return False
        
        self.key.append(val)
        self.value_index[val]=len(self.key)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.value_index:
            
            index=self.value_index[val]
            
            self.key[index-1],self.key[-1]=self.key[-1],self.key[index-1]
            self.value_index[self.key[index-1]]=index
            self.key.pop()

            del self.value_index[val]
            
            
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.key)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# ------------------------------------------------------
# 🔥 বাস্তব জীবনের অ্যাপ্লিকেশন (Insert Delete GetRandom O(1))
# ------------------------------------------------------

# 🎮 ১. গেম লুট সিস্টেম (Game Loot Drop System)
# উদাহরণঃ PUBG, Clash Royale
# - প্লেয়ার নতুন আইটেম আনলক করলে ➤ insert(item)
# - পুরাতন আইটেম বাদ দিলে ➤ remove(item)
# - র‍্যান্ডমভাবে নতুন আইটেম drop হয় ➤ getRandom()

# ⚙️ ২. লোড ব্যালেন্সার (Load Balancer in Server Cluster)
# উদাহরণঃ Google Server Farm
# - নতুন সার্ভার যুক্ত করলে ➤ insert(server_id)
# - সার্ভার ডাউন হলে ➤ remove(server_id)
# - Randomly একটিকে চুজ করে রিকোয়েস্ট পাঠানো ➤ getRandom()

# 🎰 ৩. লাকি ড্র / ক্যাসিনো অ্যাপ
# উদাহরণঃ Online Spin-to-Win
# - User রেজিস্টার করলে ➤ insert(user_id)
# - User ইনঅ্যাক্টিভ হলে ➤ remove(user_id)
# - Winner randomly pick করতে ➤ getRandom()

# 🛍️ ৪. ফ্ল্যাশ সেল বা র‍্যান্ডম পণ্যের বিজ্ঞাপন
# উদাহরণঃ Daraz বা Amazon
# - ইন স্টকে আইটেম এলে ➤ insert(product_id)
# - আউট-অফ-স্টক হলে ➤ remove(product_id)
# - হোমপেজে random পণ্য দেখাতে ➤ getRandom()

# 📱 ৫. চ্যাট অ্যাপে র‍্যান্ডম ইউজার পিং
# উদাহরণঃ Discord, Clubhouse
# - User অ্যাপে জয়েন করলে ➤ insert(user_id)
# - User লিভ করলে ➤ remove(user_id)
# - Random ভাবে একজন active user কে ping করা ➤ getRandom()

# ------------------------------------------------------
# ❗ যদি আমরা Efficient Structure না ব্যবহার করি:
# - insert() হয়তো O(1), কিন্তু remove() বা getRandom() হতে পারে O(n)
# - ফলে সিস্টেম ধীর হয়ে যাবে, বড় ডেটা হ্যান্ডল করতে পারবে না
# - latency বাড়বে, ইউজার experience খারাপ হবে
# - রিয়েল-টাইম অ্যাপ্লিকেশন যেমন গেম, লোড ব্যালেন্সার, লাকি ড্র ঠিকমতো কাজ করবে না
# - রিসোর্স অপচয় বেশি হবে
#
# ✅ তাই:
# - O(1) insert, delete, এবং getRandom এর জন্য
# - RandomizedSet বা HashMap + List কম্বিনেশন দরকার
# ------------------------------------------------------

# ✅ এইসব সকল ক্ষেত্রে দরকার:
# - O(1) সময়ে insert
# - O(1) সময়ে delete
# - O(1) সময়ে random নির্বাচন
# ➤ তাই RandomizedSet টাইপের ডেটা স্ট্রাকচার অপরিহার্য।
# ------------------------------------------------------
