class Solution:
    def trap(self, height: List[int]) -> int:
        n, water, stack = len(height), 0, []

        for i in range(n):
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[stack[-1]] < height[i]:
                    bottom = stack.pop()
                    if stack:
                        water += (min(height[i], height[stack[-1]]) - height[bottom]) * (i - stack[-1] - 1)
                stack.append(i)

        return water
