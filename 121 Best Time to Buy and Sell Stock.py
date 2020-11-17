class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result, watermark = 0, 0

        for i in range(1, len(prices)):
            watermark = max(0, watermark + prices[i] - prices[i - 1])
            result = max(result, watermark)

        return result
