class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                nums[i] = -nums[i]
            else:
                seen.add(nums[i])

        return sum(nums)
