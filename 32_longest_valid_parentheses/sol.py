# no Liana solution


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0
        dp = [0] * n
        dp[1] = 2 if s[:2] == '()' else 0
        result = max(dp[:2])

        for i in xrange(2, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif i > dp[i - 1] and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                result = max(result, dp[i])
        return result

sol = Solution()
print sol.longestValidParentheses('()(())')
