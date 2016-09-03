class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for i in range(l1 + 1)] for i in range(l2 + 1)]
        for i in range(1, l1 + 1):
            dp[0][i] = i
        for i in range(1, l2 + 1):
            dp[i][0] = i
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[l2][l1]

    def minDistance_self(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in xrange(len(word2) + 1)] for _ in xrange(len(word1) + 1)]

        for i in xrange(len(word1) + 1):
            dp[i][0] = i

        for j in xrange(len(word2) + 1):
            dp[0][j] = j

        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1],  # convert word1[:i-2] to word2[:j-2]
                                                      # then replace word1[i-1] with word2[j-1]
                                   dp[i - 1][j],      # convert word1[:i-2] to word2[:j-1]
                                                      # then delete word1[i-1]
                                   dp[i][j - 1]) + 1  # convert word1[:i-1] to word2[:j-2]
                                                      # then insert word2[j-1]
        return dp[-1][-1]
