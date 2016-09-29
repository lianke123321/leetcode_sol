# no Liana solution


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    return 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while True:
            mid = (lo + hi) >> 1
            res = guess(mid)
            if res == -1:
                hi = mid - 1
            elif res == 1:
                lo = mid + 1
            else:
                return mid
