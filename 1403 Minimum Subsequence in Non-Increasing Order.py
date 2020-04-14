class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        threshold = sum(nums) / 2
        result = []

        for item in sorted(nums, reverse=True):
            threshold -= item
            result.append(item)
            if threshold < 0:
                return result
