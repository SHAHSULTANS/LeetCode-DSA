


from typing import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.LRU=OrderedDict()

    def get(self, key: int) -> int:
        if key in self.LRU:
            self.LRU.move_to_end(key)
            return self.LRU[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self.LRU[key]=value
            self.LRU.move_to_end(key)
        else:
            if len(self.LRU)<self.capacity:
                self.LRU[key]=value
            else:
                self.LRU.popitem(last=False)
                self.LRU[key]=value
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# # param_1 = obj.get(key)
# obj.put(1,0)
# obj.put(2,0)

# print(obj.get(1))

# o=OrderedDict()
# o[1]=0
# print(o[1])
