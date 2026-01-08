

def stringPermutations(st):
    


    def per(s,track,ar):
        # print(ar)
        if len(ar)==len(st):
            print(ar.copy())
 
        for ch in s:
            if track.get(ch) is None:
                ar.append(ch)
                track[ch]=1
                per(s,track,ar)
                ar.pop()
                del track[ch]

    per(st,{},[])



stringPermutations("abcd")




