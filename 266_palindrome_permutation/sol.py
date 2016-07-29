# no Liana solution


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True

        from collections import Counter
        c = Counter([i for i in s])
        odd_freq = False
        for letter in c:
            if c[letter] % 2 != 0:
                if odd_freq:
                    return False
                else:
                    odd_freq = True
        return True

sol = Solution()
print sol.canPermutePalindrome('carerac')
