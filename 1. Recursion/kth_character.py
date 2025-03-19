import string

# print(string.ascii_lowercase)
lowercase=string.ascii_lowercase
# print(lowercase.index("z"))
# print(lowercase[25])
class Solution:
    def kthCharacter(self, k: int) -> str: 
        original_string="a"
        update_string="a"
        while(len(original_string)<k):
            for letter in original_string:
                index=(lowercase.index(letter)+1)%26
                update_string+=lowercase[index]
            original_string=update_string
        
        return original_string[k-1]
        
ob=Solution()
print(ob.kthCharacter(5))
                
                
        