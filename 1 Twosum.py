class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            if target - nums[i] in seen.keys():
                return [seen[target - nums[i]], i]
            else:
                seen[nums[i]] = i
