class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        result, window = [], deque()

        for i in range(len(nums)):
            if window and window[0] < i - k + 1:
                window.popleft()
            while window and nums[i] > nums[window[-1]]:
                window.pop()

            window.append(i)
            if i >= k - 1:
                result.append(nums[window[0]])

        return result
