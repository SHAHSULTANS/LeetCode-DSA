class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hmap={}
        for index,item in enumerate(nums):
            if item in hmap and index-hmap[item]<=k:
                return True

            hmap[item]=index

        return False

        # for index, item in enumerate(nums):
        #     nums[index]=(item,index)

        # nums.sort(key= lambda x: x[0])
        
        # for i in range(len(nums)-1):
        #     if nums[i][0]==nums[i+1][0] and abs(nums[i][1]-nums[i+1][1])<=k:
        #         return True

        # return False
        
        
        
        
 # Real-world Applications:
    # -----------------------------
    # 1. Banking / Fraud Detection:
    #    Detect if the same transaction amount occurs multiple times
    #    within 'k' transactions. This may indicate fraud or mistakes.
    #
    # 2. Social Media / Spam Detection:
    #    Detect if a user posts the same message repeatedly within
    #    'k' posts. Helps in spam prevention.
    #
    # 3. Network / Server Monitoring:
    #    Detect repeated error codes within 'k' events. Helps
    #    DevOps monitor system reliability and alert on repeated failures.
    #
    # 4. Inventory / Warehouse Management:
    #    Detect if the same item barcode is scanned multiple times
    #    within 'k' scans, preventing duplicate entries.
    #
    # 5. Online Gaming / Cheating Detection:
    #    Detect if a player repeats the same action rapidly within 'k'
    #    actions. Helps prevent bots or unfair play.