

def min_op(s1,s2,index1,index2):
    if index1==len(s1):
        return len(s2)-index2
    if index2==len(s2):
        return len(s1)-index1
    
    if s1[index1]==s2[index2]:
        return min_op(s1,s2,index1+1,index2+1)
    else:
        insert_op=1+min_op(s1,s2,index1+1,index2)
        delete_op=1+min_op(s1,s2,index1,index2+1)
        replace_op=1+min_op(s1,s2,index1+1,index2+1)
        
        return min(insert_op,delete_op,replace_op)
    
s1="table"
s2="tblemng"
print(min_op(s1,s2,0,0))