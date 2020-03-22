class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i, x in zip(index, nums):
            target.insert(i, x)

        return target
