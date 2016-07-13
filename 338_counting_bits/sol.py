# no Liana solution


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0 for _ in xrange(num + 1)]
        for i in range(num + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result

sol = Solution()
print sol.countBits(5)
