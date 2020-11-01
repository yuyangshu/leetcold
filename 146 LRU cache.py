from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.map:
            self.map.move_to_end(key)
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            self.map.move_to_end(key)
        else:
            self.map[key] = value
            if len(self.map) > self.capacity:
                self.map.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
