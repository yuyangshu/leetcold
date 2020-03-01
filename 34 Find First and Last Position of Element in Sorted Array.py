class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(i, j, target):
            while i < j:
                if nums[(i + j) // 2] >= target:
                    j = (i + j) // 2
                elif nums[(i + j) // 2] < target:
                    i = (i + j) // 2 + 1
            else:
                return i

        left = find(0, len(nums), target)

        return [left, find(left, len(nums), target + 1) - 1] if target in nums[left: left + 1] else [-1, -1]
