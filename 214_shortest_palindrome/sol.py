# no Liana solution


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        r = s[::-1]
        for i in xrange(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

sol = Solution()
print sol.shortestPalindrome("aaacecaaa")
