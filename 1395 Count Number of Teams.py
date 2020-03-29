class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        total = 0
        for mid in range(1, n - 1):
            smaller_left = len([item for item in rating[:mid] if item < rating[mid]])
            larger_left = len([item for item in rating[:mid] if item > rating[mid]])
            larger_right = len([item for item in rating[mid + 1:] if item > rating[mid]])
            smaller_right = len([item for item in rating[mid + 1:] if item < rating[mid]])

            total += smaller_left * larger_right + larger_left * smaller_right

        return total
