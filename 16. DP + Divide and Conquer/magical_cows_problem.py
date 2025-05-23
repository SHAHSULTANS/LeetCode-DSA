


def magical_cows(c,initial,query_days):
    #c==1000 cows in one farm(maximum)
    which_day_double_inital_cows_sum=[0]*11
    for each_farm_cows in initial:
        i=1
        while True:
            if each_farm_cows*pow(2,i)>C:
                which_day_double_inital_cows_sum[i]+=1
                break
            i+=1
    # print(which_day_double_inital_cows_sum)
    
    
    for day in query_days:
        need_farm_ctn=0
        for i in range(1,11,1):
            if i<=day and which_day_double_inital_cows_sum[i]>0:
                need_farm_ctn+=pow(2,(day-(i-1)))
                # print("yes")
            else:
                need_farm_ctn+=which_day_double_inital_cows_sum[i]
            
        print(need_farm_ctn)   
            
                
C=10
initial_farms=[1,2]
query_days=[1,3]



magical_cows(C,initial_farms,query_days)