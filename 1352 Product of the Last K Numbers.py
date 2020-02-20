class ProductOfNumbers:

    def __init__(self):
        self.array = []
        self.none_zeros = 0
        self.product_since_last_zero = []

    def add(self, num: int) -> None:
        self.array += [num]

        if not num:
            self.none_zeros = 0
            self.product_since_last_zero = []
        else:
            self.none_zeros += 1
            if self.product_since_last_zero:
                self.product_since_last_zero += [self.product_since_last_zero[-1] * num]
            else:
                self.product_since_last_zero = [num]

    def getProduct(self, k: int) -> int:
        if k > self.none_zeros:
            return 0
        elif k == self.none_zeros:
            return self.product_since_last_zero[-1]
        else:
            return self.product_since_last_zero[-1] // self.product_since_last_zero[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)