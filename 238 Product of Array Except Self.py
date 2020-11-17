class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before, after = [1] * n, [1] * n

        for i in range(1, n):
            before[i] = nums[i - 1] * before[i - 1]
            after[n - i - 1] = nums[n - i] * after[n - i]

        return [before[i] * after[i] for i in range(n)]
