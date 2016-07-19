# no Liana solution


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        length = len(s1)
        count = [0] * 26

        for i in xrange(length):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1

        for num in count:
            if num != 0:
                return False

        for i in xrange(1, length):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[length - i:]) and self.isScramble(s1[i:], s2[:length - i]):
                return True
        return False

sol = Solution()
print sol.isScramble('abcd', 'acbd')
