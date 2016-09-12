# no Liana solution


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        for i in xrange(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                elif len(s) < len(t):
                    return s[i:] == t[i + 1:]
                else:
                    return s[i + 1:] == t[i:]

        return True
