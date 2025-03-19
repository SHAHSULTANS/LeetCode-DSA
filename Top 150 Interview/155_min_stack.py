


class MinStack:

    def __init__(self):
        self.stock=[]
        self.minvalue=[]
        

    def push(self, val: int) -> None:
        self.stock.append(val)
        if len(self.stock)==1:
            self.minvalue.append(val)
        else:
            l=len(self.minvalue)
            # print(l)
            l=self.minvalue[l-1]
            l=min(val,l)
            self.minvalue.append(l)
            # self.minvalue.append(min(val,self.minvalue[len(self.minvalue)-1]))

    def pop(self) -> None:
        self.stock.pop()
        self.minvalue.pop()
        

    def top(self) -> int:
        return self.stock[len(self.stock)-1]
        

    def getMin(self) -> int:
        l=(len(self.stock))
        return self.minvalue[l-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
obj.push(44)
obj.push(4)
print(obj.stock)
print(obj.getMin())
obj.push(1)
print(obj.getMin())
obj.pop()
obj.pop()
print(obj.stock)
print(obj.minvalue)
print(obj.getMin())

# print(len(obj.stock))
