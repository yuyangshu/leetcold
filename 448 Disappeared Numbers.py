class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums = [0] + nums

        for i in range(len(nums)):
            while nums[i] != i:
                if nums[nums[i]] != nums[i]:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                else:
                    break

        return [index for index, item in enumerate(nums) if item != index]
