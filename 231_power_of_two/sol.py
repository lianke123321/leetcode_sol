class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n != 0:
            if n == 1:
                return True
            if n % 2 != 0:
                return False
            n /= 2

    def isPowerOfTwo_self(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        n = bin(n)[3:]
        return n == '0' * len(n)

        # one-liner
        # return n > 0 and n & (n - 1) == 0
