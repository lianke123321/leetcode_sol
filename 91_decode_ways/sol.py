class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        r1 = 1
        r2 = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                r1 = 0
            if s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6':
                r1 = r1 + r2
                r2 = r1 - r2
            else:
                r2 = r1
        return r1

    def numDecodings_self(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s)
        if count == 0:
            return 0

        dp = [0 for _ in xrange(count + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in xrange(2, count + 1):
            single = int(s[i-1:i])
            double = int(s[i-2:i])
            if 1 <= single <= 9:
                dp[i] += dp[i - 1]
            if 10 <= double <= 26:
                dp[i] += dp[i - 2]

            if dp[i] == 0:
                return 0

        return dp[count]

sol = Solution()
print sol.numDecodings('19001')
