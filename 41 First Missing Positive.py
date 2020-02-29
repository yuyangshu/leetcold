class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [0] + nums
        
        for i in range(1, n + 1):
            while nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(1, n + 1):
            if nums[i] != i:
                return i
        else:
            return n + 1
