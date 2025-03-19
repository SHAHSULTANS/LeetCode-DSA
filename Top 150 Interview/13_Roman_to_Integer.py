

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        
        ans=0
        index=0
        
        while index<len(s):
            if(index<len(s)-1):
                check=s[index]+s[index+1]
                # print(check)
                # print(type(check))
                if(roman_to_integer.get(check)):
                    ans+=roman_to_integer[check]
                    index+=2
                else:
                    ans+=roman_to_integer[s[index]]
                    index+=1
            else:
                ans+=roman_to_integer[s[index]]
                index+=1   
        
        return ans


s= "MCMXCIV"
ob=Solution()
ob.romanToInt(s)


    
    
    