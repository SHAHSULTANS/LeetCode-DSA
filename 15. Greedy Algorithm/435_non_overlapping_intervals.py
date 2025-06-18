
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(reverse=True)
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        ctn=1
        index=0

        for i in range(1,len(intervals)):
            if intervals[index][1]<=intervals[i][0]:            
                ctn+=1
                index=i
                print(i)
            
        return len(intervals)-ctn

        

# Real-World Applications of "Erase Overlap Intervals" Problem

# 1. Operations Research:
#    - বিভিন্ন কাজ বা জব-এর টাইম স্লট অপ্টিমাইজ করতে ব্যবহৃত হয়।
#    - যেমন: একটি মেশিনে কয়টি কাজ করানো যাবে যাতে টাইম স্লট overlap না করে।

# 2. Computer Systems / CPU Scheduling:
#    - Operating system-এ বিভিন্ন প্রোসেস বা টাস্কের execution টাইম ঠিক করতে হয়।
#    - এই সমস্যা ব্যবহার করে determine করা হয় কোন job গুলো conflict ছাড়া চলবে।

# 3. Air Traffic Control:
#    - একটি রানওয়ে দিয়ে একসাথে কেবল একটি ফ্লাইট টেক-অফ বা ল্যান্ড করতে পারে।
#    - overlapping টাইম স্লট ফ্লাইট detect করে কাদের রিসিডিউল বা বাদ দিতে হবে তা নির্ধারণে ব্যবহৃত।

# 4. Event Planning:
#    - একাধিক ইভেন্ট একই ভেনুতে করতে হলে সময় conflict হতে পারে।
#    - এই algorithm দিয়ে determine করা হয় কোন event গুলো রাখা যাবে overlap ছাড়া।

# 5. Meeting Room Booking:
#    - একটি মিটিং রুমে একাধিক মিটিং হলে টাইম clash হতে পারে।
#    - এই সমস্যা ব্যবহার করে দেখা হয় কয়টি মিটিং বাদ দিলে conflict মুক্ত schedule পাওয়া যায়।

# 6. Doctor’s Appointment System:
#    - ডাক্তার প্রতিদিন নির্দিষ্ট সংখ্যক রোগী দেখতে পারেন।
#    - overlapping অ্যাপয়েন্টমেন্ট detect করে সেগুলো অপ্টিমাইজ করা হয়।

# 7. TV Advertisement Slot Management:
#    - TV চ্যানেলে একই সময়ে একাধিক কোম্পানি বিজ্ঞাপন দিতে চাইলে overlap হয়।
#    - conflict ছাড়া সর্বোচ্চ কতগুলো বিজ্ঞাপন দেখানো যাবে তা নির্ধারণে ব্যবহৃত।

# 8. Traffic Signal Scheduling:
#    - একাধিক রোড থেকে গাড়ি আসলে তাদের পার হওয়ার টাইম স্লট নির্ধারণ করতে হয়।
#    - overlapping স্লট ফিল্টার করে conflict মুক্ত সিগনাল টাইম তৈরি করতে সাহায্য করে।

# Summary:
# এই সমস্যাটি একটি greedy approach ব্যবহার করে এবং মূলত conflict-free scheduling, 
# resource optimization, এবং efficient allocation-এ বাস্তব প্রয়োগ রয়েছে।
