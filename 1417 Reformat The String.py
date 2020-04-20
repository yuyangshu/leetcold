class Solution:
    def reformat(self, s: str) -> str:
        def concatenate(A, B, extra):
            result = []
            for i in range(len(A)):
                result.append(A[i])
                result.append(B[i])
            result.append(extra)

            return "".join(result)

        chars = [c for c in s if ord('a') <= ord(c) <= ord('z')]
        nums = [c for c in s if ord('0') <= ord(c) <= ord('9')]

        if len(chars) - len(nums) == 1:
            return concatenate(chars[:-1], nums, chars[-1])
        elif len(nums) - len(chars) == 1:
            return concatenate(nums[:-1], chars, nums[-1])
        elif len(chars) == len(nums):
            return concatenate(chars, nums, "")
        else:
            return ""
