class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = current = 0
        n = len(nums)

        for current in range(n):
            if nums[current]:
                nums[pointer] = nums[current]
                pointer += 1
        else:
            while pointer < n:
                nums[pointer] = 0
                pointer += 1
