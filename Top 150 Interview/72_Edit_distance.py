class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        def edit_distance(s1,s2,i,j,memo):
            if len(s2)==j:
                return len(s1)-i
            if len(s1)==i:
                return len(s2)-j
            
            if (i,j) in memo:
                return memo[(i,j)]    
            
            if s1[i]==s2[j]:
                memo[(i,j)]=edit_distance(s1,s2,i+1,j+1,memo)
                return memo[(i,j)]
            else:
                insert_op= 1 + edit_distance(s1,s2,i,j+1,memo)
                delete_op= 1 + edit_distance(s1,s2,i+1,j,memo)
                replace_op= 1 + edit_distance(s1,s2,i+1,j+1,memo)
                
                memo[(i,j)]=min(insert_op,delete_op,replace_op)
                return memo[(i,j)]
            
        return edit_distance(word1,word2,0,0,{})