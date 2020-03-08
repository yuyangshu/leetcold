class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        watermark = count = 0

        for i in range(len(light)):
            if light[i] > watermark:
                watermark = light[i]

            if watermark == i + 1:
                count += 1

        return count
