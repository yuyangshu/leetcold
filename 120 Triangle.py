class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = [triangle[0][0]]

        for i in range(1, len(triangle)):
            temp = [0] * len(triangle[i])

            temp[0] = prev[0] + triangle[i][0]
            temp[-1] = prev[len(triangle[i]) - 2] + triangle[i][-1]

            for j in range(1, len(triangle[i]) - 1):
                temp[j] = min(prev[j - 1], prev[j]) + triangle[i][j]

            prev = temp

        return min(prev)
