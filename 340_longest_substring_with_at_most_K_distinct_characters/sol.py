# no Liana solution
from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res, hashmap = 0, defaultdict(int)
        start = 0
        for i in xrange(len(s)):
            hashmap[s[i]] += 1
            while len(hashmap) > k:
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res

sol = Solution()
print sol.lengthOfLongestSubstringKDistinct('eceba', 2)
