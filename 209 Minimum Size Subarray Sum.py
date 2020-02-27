class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        length = 0

        if nums:
            n, st, ed, total = len(nums), 0, 0, 0
            
            while ed < n:
                total += nums[ed]
                ed += 1

                while total >= s:
                    if not length or length > ed - st:
                        length = ed - st
        
                    total -= nums[st]
                    st += 1

        return length
