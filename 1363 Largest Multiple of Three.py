class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        from collections import Counter

        def translate(digits: List[int]) -> str:
            if not digits:
                return ""

            result = 0
            for digit in digits:
                result = result * 10 + digit

            return str(result)

        digits = sorted(digits, reverse=True)
        total = sum(digits)
        counts = Counter(digits)

        if not total % 3:
            return translate(digits)
        else:
            target = total % 3
            if counts[target] >= 1:
                for i in range(len(digits) - 1, -1, -1):
                    if digits[i] % 3 == target:
                        return translate(digits[:i] + digits[i + 1:])
            elif counts[3 - target] >= 2:
                to_return = False
                for i in range(len(digits) - 1, -1, -1):
                    if digits[i] % 3 == 3 - target:
                        if not to_return:
                            digits = digits[:i] + digits[i + 1:]
                            to_return = True
                        else:
                            return translate(digits[:i] + digits[i + 1:])
            else:
                return ""
