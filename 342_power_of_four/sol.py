# no Liana solution


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num & (num - 1) == 0 and (num - 1) % 3 == 0

    def isPowerOfFour_2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        num = bin(num)[3:]
        if num != '0' * len(num) or len(num) % 2 != 0:
            return False
        else:
            return True
