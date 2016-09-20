# no Liana solution


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in xrange(len(s)):
            result += (ord(s[i]) - ord('A') + 1) * (26 ** (len(s) - i - 1))
        return result

sol = Solution()
print sol.titleToNumber('AB')
