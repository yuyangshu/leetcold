class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        from collections import Counter

        stock, result = sorted(Counter(inventory).most_common(), key=lambda x: x[0], reverse=True), 0

        while orders > 0:
            gap = stock[0][0] - (stock[1][0] if len(stock) > 1 else 0)
            if gap * stock[0][1] < orders:
                result += (stock[0][0] + stock[1][0] + 1) * gap * stock[0][1] // 2
                orders -= gap * stock[0][1]
                stock = [(stock[1][0], stock[1][1] + stock[0][1])] + stock[2:]
            else:
                # gap * stock[0][1] == orders
                batch = orders // stock[0][1]
                result += (stock[0][0] + stock[0][0] - batch + 1) * batch * stock[0][1] // 2 + (stock[0][0] - batch) * (orders % stock[0][1])
                return result % (pow(10, 9) + 7)
