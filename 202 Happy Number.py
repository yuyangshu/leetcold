class Solution:
    def isHappy(self, n: int) -> bool:
        def get_digits(number: int) -> tuple:
            result = []
            while number:
                result.append(number % 10)
                number = number // 10

            return tuple(sorted(result))

        seen = set()
        digits = get_digits(n)

        while digits not in seen:
            if digits == (1,):
                return True
            else:
                seen.add(digits)
                digits = get_digits(sum([digit ** 2 for digit in digits]))
        else:
            return False
