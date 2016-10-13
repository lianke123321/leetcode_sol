# no Liana solution
from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, hashmap = 0, defaultdict(int)
        start = 0
        for i in xrange(len(s)):
            hashmap[s[i]] += 1
            while len(hashmap) > 2:
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res
