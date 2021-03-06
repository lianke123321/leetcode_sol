# no Liana solution


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n &= (n - 1)
            res += 1
        return res
