# https://leetcode.com/problems/count-primes/
# Count the number of prime numbers less than a non-negative number, n.
# Brilliant Solution from others, avoided primes check to reduce time complexity

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

        
if __name__=="__main__":
    obj = Solution()
    param_1 = obj.countPrimes(999983)
    print(param_1)
