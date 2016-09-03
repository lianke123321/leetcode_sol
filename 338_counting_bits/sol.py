# no Liana solution


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in xrange(1, num + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result

sol = Solution()
print sol.countBits(5)
