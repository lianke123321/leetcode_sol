# no Liana solution


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sp, pp, match, star_idx = 0, 0, 0, -1

        while sp < len(s):
            if pp < len(p) and (p[pp] == '?' or p[pp] == s[sp]):
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == '*':
                star_idx = pp
                match = sp
                pp += 1
            elif star_idx != -1:
                pp = star_idx + 1
                match += 1
                sp = match
            else:
                return False

        while pp < len(p) and p[pp] == '*':
            pp += 1

        return pp == len(p)
