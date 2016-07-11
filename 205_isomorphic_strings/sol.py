# no Liana solution


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]
            elif hashmap[s[i]] != t[i]:
                return False

        hashmap = {}
        for i in range(len(t)):
            if t[i] not in hashmap:
                hashmap[t[i]] = s[i]
            elif hashmap[t[i]] != s[i]:
                return False

        return True
