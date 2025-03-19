

import array


myarray=array.array('i',[])


days=int(input("How days do you want to enter?: "))

for i in range(days):
    temp=int(input(f"Enter Day's{i+1} temperature?: "))
    myarray.append(temp)

avg_temp=round(sum(myarray)/days,2)

count=sum(temp>avg_temp for temp in myarray)

print()
print(f"Avg Temperature is: {(sum(myarray)/days) :.2f}")
print(f"{count} Days had greater temperature than AVG.")


