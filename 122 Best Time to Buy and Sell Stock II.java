class Solution {
    public int maxProfit(int[] prices) {
        int result = 0, watermark = prices[0];

        for (int i = 1; i < prices.length; i ++) {
            if (prices[i] > watermark) {
                result += prices[i] - watermark;
            }

            watermark = prices[i];
        }

        return result;
    }
}
