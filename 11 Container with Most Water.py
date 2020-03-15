class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        most_water = min(height[i], height[j]) * j
        
        while i < j:
            most_water = max(most_water, min(height[j], height[i]) * (j - i))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return most_water
