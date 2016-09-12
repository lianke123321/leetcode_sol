# no Liana solution


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        hashmap, missing = Counter(t), len(t)
        i, start, end = 0, 0, 0
        for j in xrange(1, len(s) + 1):
            missing -= hashmap[s[j - 1]] > 0
            hashmap[s[j - 1]] -= 1
            if not missing:
                while i < j and hashmap[s[i]] < 0:
                    hashmap[s[i]] += 1
                    i += 1
                if not end or j - i < end - start:
                    start, end = i, j
        return s[start:end]

sol = Solution()
print sol.minWindow("a", "aa")
