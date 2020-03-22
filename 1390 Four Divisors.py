class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        import math

        total = 0
        for x in nums:
            divisors = set()
            for i in range(1, math.floor(math.sqrt(x)) + 1):
                if x % i == 0:
                    divisors.add(i)
                    divisors.add(x // i)
                    if len(divisors) > 4:
                        break
            else:
                if len(divisors) == 4:
                    total += sum(divisors)

        return total



# own solution, exceeds time limit

# class Solution:
#     def sumFourDivisors(self, nums: List[int]) -> int:
#         checker = [True] * 50000
        
#         primes = [2]
#         for i in range(3, 50000, 2):
#             if checker[i]:
#                 primes.append(i)
#                 target = i * 2
#                 while target < 50000:
#                     checker[target] = False
#                     target += i

#         total = 0
#         for x in nums:
#             for k in primes:
#                 if x % k == 0 and k != x // k and (x // k in primes or x // k == k ** 2):
#                     total += 1 + k + x // k + x
#                     break

#         return total
