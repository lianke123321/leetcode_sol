# no Liana solution


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = len(s)
        if c < 2 or s == s[::-1]:
            return 0

        # check if cut could be 1
        for i in xrange(1, c):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        # otherwise, run the algo
        dp = [i - 1 for i in xrange(c + 1)]
        for i in xrange(2, c + 1):
            for j in xrange(i):
                if self.isPalindrome(s[j:i]):
                    dp[i] = min(dp[i], dp[j] + 1)

        # TODO: further optimization

    def isPalindrome(self, s):
        if len(s) < 2:
            return True
        else:
            return s[:len(s) / 2] == s[-1:len(s) / 2 + len(s) % 2 - 1:-1]

sol = Solution()
print sol.minCut("ababababababababababababcbabababababababababababa")
