# my solution is the same with Liana's


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n > 0:
            n -= 1
            result = chr(n % 26 + ord('A')) + result
            n /= 26
        return result
