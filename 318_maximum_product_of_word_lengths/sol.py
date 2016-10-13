# no Liana solution


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        vals = [0] * len(words)
        for i in xrange(len(words)):
            for c in set(words[i]):
                vals[i] |= (1 << (ord(c) - ord('a')))

        res = 0
        for i in xrange(len(words)):
            for j in xrange(i + 1, len(words)):
                if vals[i] & vals[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

sol = Solution()
print sol.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
