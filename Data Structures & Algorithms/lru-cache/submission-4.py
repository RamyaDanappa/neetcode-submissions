from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        #hit and move to hit value
        self.cache.move_to_end(key)
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #hit_value 
            self.cache[key] = value
            self.cache.move_to_end(key)
        elif key not in self.cache:
            #check cache is  have space 
            if len(self.cache)<self.capacity:
                self.cache[key]=value
            else:
                self.cache.popitem(last=False)
                self.cache[key]=value
        
