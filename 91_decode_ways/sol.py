class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        r1 = 1
        r2 = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                r1 = 0
            if s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6':
                r1 = r1 + r2
                r2 = r1 - r2
            else:
                r2 = r1
        return r1

    def numDecodings_self(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s)
        if count == 0 or s[0] == '0':
            return 0

        r1, r2 = 1, 1

        for i in xrange(2, count + 1):
            new_r2 = 0
            single, double = int(s[i-1:i]), int(s[i-2:i])
            if 1 <= single <= 9:
                new_r2 += r2
            if 10 <= double <= 26:
                new_r2 += r1

            if new_r2 == 0:
                return 0
            r1, r2 = r2, new_r2
        return r2

sol = Solution()
print sol.numDecodings_self('19231')
