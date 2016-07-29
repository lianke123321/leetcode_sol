class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        result = ''
        digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        digit = digit[0: n]
        i = n - 1
        k -= 1
        while k > 0:
            num = k / math.factorial(i)
            k -= num * math.factorial(i)
            if k == 0:
                num -= 1
            result += str(digit[num])
            del digit[num]

            i -= 1
        while digit:
            result += str(digit.pop())
        return result

    def getPermutation_self(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return '1'

        from math import factorial
        result = ''
        candidates = [i for i in xrange(1, n + 1)]
        denominator = factorial(n - 1)

        k  -= 1
        for i in xrange(1, n):
            index = k / denominator
            result += str(candidates.pop(index))
            k %= denominator
            denominator /= (n - i)
        return result + str(candidates[0])

sol = Solution()
print sol.getPermutation_self(3, 1)
