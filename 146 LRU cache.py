class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.first = None
        self.last = None
        self.map = dict()

    def get(self, key: int) -> int:
        if key in self.map.keys():
            self._move_to_end(key)
            return self.last.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            node = self.map[key].value = value
            self._move_to_end(key)
        else:
            node = Node(key, value)
            if not self.length:
                self.first = node
            else:
                node.previous = self.last
                self.last.next = node

            self.length += 1
            self.last = node
            self.map[key] = node

            if self.length > self.capacity:
                self.length -= 1
                self.map.pop(self.first.key)
                self.first = self.first.next

    def _move_to_end(self, key: int) -> None:
        node = self.map[key]

        if node != self.last:
            if node == self.first:
                self.first = node.next
            if node.next:
                node.next.previous = node.previous
            if node.previous:
                node.previous.next = node.next

            self.last.next = node
            node.previous = self.last
            node.next = None
            self.last = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)