class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap = {}
        for c in s:
            if c not in hashMap:
                hashMap[c] = 1
            else:
                hashMap[c] += 1
        for c in t:
            if c not in hashMap:
                return False
            else:
                hashMap[c] -= 1
            # if hashMap[c] < 0:
            # return False
        for key in hashMap:
            if hashMap[key] != 0:
                return False
        return True

    def isAnagram_self(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        c1, c2 = Counter([i for i in s]), Counter([i for i in t])
        if len(c1) != len(c2):
            return False
        else:
            for k in c1:
                if k not in c2 or c1[k] != c2[k]:
                    return False
        return True
