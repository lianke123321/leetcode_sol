class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        f = [False for i in range(0, len(s) + 1)]
        f[0] = True
        for i in range(1, len(s) + 1):
            # for j in range(0, i):
            j = i - 1
            while j >= 0:
                if f[j] and s[j: i] in wordDict:
                    f[i] = True
                    break
                j -= 1
        return f[len(s)]

    def wordBreak_self(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in xrange(1, len(s) + 1):
            j = i - 1
            while j >= 0:
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                j -= 1
        return dp[-1]
