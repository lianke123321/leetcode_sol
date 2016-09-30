# no Liana solution


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ord(t[-1])
        for i in xrange(len(s)):
            res ^= ord(s[i])
            res ^= ord(t[i])
        return chr(res)

sol = Solution()
print sol.findTheDifference('abcd', 'abcde')
