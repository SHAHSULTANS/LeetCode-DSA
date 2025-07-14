import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delaytime=[float('inf') for _ in range(n+1)]

        
        graph=[[] for _ in range(n+1)]
        # print(graph)
        for edge in times:
            # print(edge)
            graph[edge[0]].append((edge[1],edge[2]))
            # print(graph)
        
        hp=[]
        heapq.heappush(hp,(0,k))
        delaytime[k]=0
        
        # print(hp)
        while hp:
            min_value_node=heapq.heappop(hp)
            # print(min_value_node)  
            for adjacent in graph[min_value_node[1]]:
                node=adjacent[0]
                time_weight=min_value_node[0]+adjacent[1]
                if time_weight<delaytime[node]:
                    delaytime[node]=time_weight
                    heapq.heappush(hp,(time_weight,node))
                    
                    
        ans=float('-inf')
        for i in range(1,n+1):
            if delaytime[i]== float('inf'):
                return -1
            ans=max(ans,delaytime[i])
            
        return ans
                   
                   
# ============================================
# 📡 Dijkstra Algorithm (networkDelayTime) এর বাস্তব জীবনের ব্যবহার
# ============================================

# ✅ ১. ইন্টারনেট রাউটিং (Internet Routing):
# প্রতিটি রাউটার অন্য রাউটারে ডেটা পাঠায় — কিন্তু কোন রাস্তায় কম সময় লাগবে তা বের করতে হয়।
# Dijkstra অ্যালগরিদম ব্যবহার করে সবচেয়ে কম latency-র পথ বের করা হয়।

# 🧾 উদাহরণ: Router R1 থেকে R4 এ ডেটা পাঠাতে R1→R2→R4 = 10ms হলে,
# Dijkstra ব্যবহার না করলে R1→R3→R4 = 50ms এর মতো সময়ও লাগতে পারে।

# ✅ ২. গুগল ম্যাপস / GPS সিস্টেমে পথ বের করা:
# কোন রাস্তা দিয়ে সবচেয়ে কম সময় লাগবে — এটা Dijkstra দিয়েই হিসাব করা হয়।

# 🧾 উদাহরণ: 
# Ambulance কে quickest route দেখাতে Google Maps “shortest delay path” বের করে।

# ✅ ৩. ডিসট্রিবিউটেড সার্ভার সিস্টেম (Distributed Systems):
# যখন একটি সার্ভার অন্য সার্ভারে কাজ পাঠায়, তখন কোনটাতে আগে যাবে সেটার জন্য delay-aware সিদ্ধান্ত নিতে হয়।

# 🧾 উদাহরণ: 
# Cloud Server A → B = 2s, A → C = 5s → তাহলে B আগে execute করবে।

# ✅ ৪. স্মার্ট ইলেকট্রিক গ্রিড (Smart Power Grid):
# বিদ্যুৎ কোন সাব-স্টেশনে আগে পৌঁছাবে এবং কত সময় লাগবে — সেটা বুঝতে delay-ভিত্তিক হিসাব দরকার হয়।

# 🧾 উদাহরণ: 
# Main Station → Sub A = 1s, Sub B = 4s → তাহলে Sub A আগে পাওয়ার পাবে।

# ✅ ৫. কাস্টমার সার্ভিস / কল সেন্টার:
# আন্তর্জাতিক ব্রাঞ্চগুলোর মধ্যে মেসেজ পাঠাতে সময় লাগে। কে আগে পাবে সেটা জানতে delay graph দরকার।

# 🧾 উদাহরণ: 
# Head Office → Dubai → India → Japan = 6s → Dijkstra দিয়ে সবচেয়ে কম সময়ে পৌঁছাবে কোন দেশে সেটা বোঝা যায়।

# ✅ ৬. ডেলিভারি রুট অপটিমাইজেশন (Delivery / Logistics):
# একটি গুদাম থেকে বিভিন্ন শহরে পণ্য পাঠাতে সবচেয়ে কম সময় কোন রুটে লাগবে?

# 🧾 উদাহরণ: 
# Central Hub → City A = 2hr, City B = 5hr → Delivery দ্রুত করতে shortest delay রুট বের করা দরকার।

# ============================================
# ⚠️ এই অ্যালগরিদম ছাড়া কী হতে পারে? (Without Dijkstra)
# ============================================

# ❌ রাউটার ভুল রাস্তা বেছে নেবে → নেটওয়ার্ক স্লো হয়ে যাবে
# ❌ জরুরি অ্যাম্বুলেন্স ভুল পথে যাবে → জীবন রক্ষা করা সম্ভব হবে না
# ❌ সার্ভার সিঙ্ক হবে না → তথ্য mismatch বা error হবে
# ❌ পাওয়ার গ্রিড দেরিতে বিদ্যুৎ দেবে → blackout বা ভোল্টেজ ড্রপ হবে
# ❌ ডেলিভারি দেরিতে পৌঁছাবে → কাস্টমার অসন্তুষ্ট হবে, টাকা নষ্ট হবে

# ✅ তাই Dijkstra অ্যালগরিদম ব্যবহার করে সঠিক সময়ে, সঠিক জায়গায় পৌঁছানো নিশ্চিত করা হয়।

                
