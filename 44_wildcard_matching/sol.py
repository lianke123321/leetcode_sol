# no Liana solution


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        c = len(s)
        dp = [True] + [False] * c

        for letter in p:
            if letter == '*':
                for i in xrange(1, c + 1):
                    dp[i] = dp[i] or dp[i - 1]
            else:
                for i in reversed(xrange(c)):
                    dp[i + 1] = dp[i] and (letter == s[i] or letter == '?')
            dp[0] = dp[0] and letter == '*'

        return dp[-1]
