from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_map=Counter(t)
        # print(target_map)
        
        our_map={}
        start = float('-inf') 
        end = float('inf')

        i=0
        left_window=0
        
        
        def matches(our_map, target_map):
            for key in target_map:
                if key not in our_map:
                    return False
                if our_map[key] < target_map[key]:
                    return False
            return True

        
        # while i<len(s)-len(t)+1:
        #     our_map[s[i]]=our_map.get(s[i],0)+1
        #     i+=1
        #     # print(our_map.items() & target_map.items())
        #     if (our_map.items() & target_map.items())==target_map.items():
        #         flag=True
        #         break
            
        # if flag:
        #     start=left_window
        #     end=i
            
        while i<len(s):
            
            while(matches(our_map,target_map)):
                our_map[s[left_window]]-=1
                left_window+=1
                
            our_map[s[i]]=our_map.get(s[i],0)+1
            i+=1
            # print(our_map)
            
            if matches(our_map,target_map):
                # print("before ",our_map)
                while(matches(our_map,target_map)):
                    our_map[s[left_window]]-=1
                    left_window+=1
                    # print("yes")
                # print("after ",our_map)

                our_map[s[left_window-1]]=our_map.get(s[left_window-1],0)+1
                left_window-=1
                
                # print("after ",our_map)
                # print(left_window)
                
                # print(s[left_window:i])
                if (i-left_window)<(end-start):
                    # print(s[left_window:i])
                    start=left_window
                    end=i
        
        # print(start," ",end)
        if start>=0 and end>=0:            
            return "".join(s[start:end])
        
        return ""
        