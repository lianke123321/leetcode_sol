# no Liana solution


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 10

        tmp = 9
        total = 10
        for i in range(2, n + 1):
            if i == 11:
                return total
            tmp *= (11 - i)
            total += tmp
        return total

sol = Solution()
print sol.countNumbersWithUniqueDigits(11)
