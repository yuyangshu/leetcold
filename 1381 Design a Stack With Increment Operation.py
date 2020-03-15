class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.array = []

    def push(self, x: int) -> None:
        if len(self.array) < self.size:
            self.array.append(x)

    def pop(self) -> int:
        if len(self.array) > 0:
            return self.array.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.array))):
            self.array[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
