class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, nums, results = len(nums), sorted(nums), []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            l, r, target = i + 1, n - 1, -nums[i]

            while l < r:
                if nums[l] + nums[r] == target:
                    results.append([-target, nums[l], nums[r]])
                    while l < n - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    l, r = l + 1, r - 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return results
