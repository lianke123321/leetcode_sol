# no Liana solution

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo = 1
        hi = num
        while lo <= hi:
            mid = (lo + hi) / 2
            if mid * mid > num:
                hi = mid - 1
            elif mid * mid < num:
                lo = mid + 1
            else:
                return True

        return False


sol = Solution()
print sol.isPerfectSquare(5)
