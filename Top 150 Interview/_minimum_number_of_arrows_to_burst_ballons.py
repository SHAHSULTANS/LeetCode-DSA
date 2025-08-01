class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        # print(points)

        arrow=1
        j=0
        for i in range(1,len(points)):
            if points[i][0]<=points[j][1]:
                continue

            arrow+=1
            j=i

        return arrow




# ============================================================
# Application 1: Fire Alarm / Security Sensor Coverage
# ------------------------------------------------------------
# ভবনের দেয়ালে অনেক ফায়ার এলার্ম বা সেন্সর আছে। 
# প্রতিটি সেন্সরের কভারেজ এলাকা একটি ইন্টারভ্যাল হিসেবে ধরা হয়।
# আমাদের লক্ষ্য কম সংখ্যক এলার্ম বসিয়ে পুরো এলাকা ঢেকে ফেলা।
#
# balloons = [ [start_coverage, end_coverage], ... ]
# arrow = একটি সেন্সর বা এলার্মের অবস্থান
# ============================================================


# ============================================================
# Application 2: Office Wi-Fi Router Placement
# ------------------------------------------------------------
# অফিসের বিভিন্ন জায়গায় Wi-Fi রাউটারের সিগন্যাল একটি নির্দিষ্ট রেঞ্জে কাজ করে।
# আমরা কম সংখ্যক রাউটার বসিয়ে পুরো অফিসের কভারেজ নিশ্চিত করতে চাই।
#
# balloons = [ [start_signal_range, end_signal_range], ... ]
# arrow = রাউটারের অবস্থান
# ============================================================


# ============================================================
# Application 3: Meeting Room Scheduling (Interval Scheduling)
# ------------------------------------------------------------
# বিভিন্ন মিটিংয়ের সময় নির্দিষ্ট থাকে। 
# সর্বনিম্ন সংখ্যক রুম ব্যবহার করেই সব মিটিং করাতে হবে।
#
# balloons = [ [meeting_start, meeting_end], ... ]
# arrow = একটি রুমের জন্য সময় বরাদ্দ
# ============================================================


# ============================================================
# Application 4: Fire Exit Planning in Buildings
# ------------------------------------------------------------
# ভবনে ফায়ার এক্সিটের সংখ্যা কম রাখতে হবে কিন্তু পুরো ভবন ঢেকে ফেলতে হবে।
#
# balloons = [ [start_safe_zone, end_safe_zone], ... ]
# arrow = ফায়ার এক্সিটের অবস্থান
# ============================================================


# ============================================================
# Application 5: Network Intrusion Detection System (NIDS)
# ------------------------------------------------------------
# নেটওয়ার্কে বিভিন্ন রুল/প্যাটার্ন থাকে নির্দিষ্ট IP বা টাইম রেঞ্জে।
# কম সংখ্যক চেক পয়েন্ট বসিয়ে যত বেশি রুল কভার করতে হয়।
#
# balloons = [ [ip_range_start, ip_range_end], ... ] বা [time_start, time_end]
# arrow = চেক পয়েন্ট ইনস্পেকশন পজিশন
# ============================================================


# ============================================================
# Application 6: Distributed Systems Task Scheduling
# ------------------------------------------------------------
# একাধিক টাস্কের নির্দিষ্ট সময়সীমা থাকে, কম সংখ্যক প্রসেসর দিয়ে সব কাজ শেষ করতে হবে।
#
# balloons = [ [task_start_time, task_end_time], ... ]
# arrow = একটি প্রসেসর বা থ্রেড
# ============================================================


# ============================================================
# Application 7: Database Lock Management
# ------------------------------------------------------------
# ডাটাবেজে বিভিন্ন ট্রানজেকশনের জন্য লক সময় নির্দিষ্ট থাকে।
# লকগুলো সঠিকভাবে ম্যানেজ করে ডেডলক এড়াতে হবে, কম সংখ্যক লক প্রয়োগ করতে হবে।
#
# balloons = [ [lock_start_time, lock_end_time], ... ]
# arrow = একটি লক সেটিং বা ম্যানেজমেন্ট পজিশন
# ============================================================


# ============================================================
# Application 8: Video Streaming Buffer Management
# ------------------------------------------------------------
# ভিডিও স্ট্রিমিংয়ে বিভিন্ন ফ্রেম ডাউনলোডের সময় নির্দিষ্ট।
# কম সংখ্যক বাফার রিকোয়েস্ট দিয়ে বেশি ফ্রেম কভার করতে হবে।
#
# balloons = [ [frame_download_start, frame_download_end], ... ]
# arrow = বাফার রিকোয়েস্ট সময়
# ============================================================


# ============================================================
# Application 9: Software Testing - Test Case Scheduling
# ------------------------------------------------------------
# অনেক টেস্ট কেস আছে, প্রত্যেকের রান টাইম নির্দিষ্ট।
# কম সংখ্যক টেস্টিং সেশন দিয়ে সব টেস্ট কেস সম্পন্ন করতে হবে।
#
# balloons = [ [test_start_time, test_end_time], ... ]
# arrow = একটি টেস্টিং সেশন বা সময়
# ============================================================


# ============================================================
# Application 10: Power Grid Maintenance Scheduling
# ------------------------------------------------------------
# পাওয়ার গ্রিডে রক্ষণাবেক্ষণের কাজের সময়সীমা নির্দিষ্ট।
# কম সংখ্যক টিম/শিফটে এই কাজগুলো শেষ করতে হবে।
#
# balloons = [ [maintenance_start, maintenance_end], ... ]
# arrow = একটি টিমের কাজের সময়
# ============================================================
