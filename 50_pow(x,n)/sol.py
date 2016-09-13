class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            n = - n
            x = 1 / x
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x * x, n / 2)


class Solution_self:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            n = -n
            x = 1 / x

        return self.myPow(x * x, n >> 1) if n % 2 == 0 \
            else x * self.myPow(x * x, n >> 1)

sol = Solution_self()
print sol.myPow(2.1, 3)
