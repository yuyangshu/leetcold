class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] + [float("-inf")] * (len(nums) - 1)
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i - 1]) + nums[i]

        return max(dp)
