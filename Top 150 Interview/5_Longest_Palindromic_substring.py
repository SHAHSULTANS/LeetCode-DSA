class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        # if length==1:
        #     return 1
        # if length==2:
        #     if s[0]==s[1]:
        #         return 2
        #     else:
        #         return 1
        
            
        ans=1
        palindromic_left_index_of_substring=0
        
        for index in range(length):
            #CONSIDER EVEN LENGTH OF SUBSTRING.
            i=index
            j=index+1
            count=0
            while(i>=0 and j<length):
                if s[i]!=s[j]:
                    break
                i-=1
                j+=1
                count+=1
             
            # if flag:
            if count*2>ans:
                ans=count*2
                palindromic_left_index_of_substring=(index-count)+1


            #CONSIDER ODD LENGTH SUBSTRING    
            i=index-1
            j=index+1 
            count=0
            while(i>=0 and j<length):
                if s[i]!=s[j]:
                    break
                i-=1
                j+=1
                count+=1
            
            if (count*2)+1>ans:
               ans=count*2+1
               palindromic_left_index_of_substring=index-count

        # print(ans)
        right_index_of_substring=palindromic_left_index_of_substring+ans        
        return s[palindromic_left_index_of_substring:right_index_of_substring]