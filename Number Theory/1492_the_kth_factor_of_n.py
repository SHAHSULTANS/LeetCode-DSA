class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        font=[]
        back=[]
        i=1
        while(i*i<=n):
            if n%i==0:
                font.append(i)
                if i!=(n//i):
                    back.append(n//i)
            i+=1

        back.reverse()
        # print(back)
        font+=back
        # print(font)
        if len(font)>=k:
            return font[k-1]

        return -1