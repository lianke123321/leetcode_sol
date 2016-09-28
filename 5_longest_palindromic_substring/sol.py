class Solution:
    def isPalindromic(self, s):
        result = True
        length = len(s)
        for i in range(length / 2):
            if s[i] != s[length - 1 - i]:
                result = False
                break
        return result

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_index = 0
        max_length = 0
        for i in range(len(s)):
            if self.isPalindromic(s[i - max_length: i + 1]):
                longest_index = i - max_length
                max_length = max_length + 1
            elif i - max_length - 1 >= 0 and self.isPalindromic(s[i - max_length - 1: i + 1]):
                longest_index = i - max_length - 1
                max_length = max_length + 2

        return s[longest_index:longest_index + max_length]


class Solution_self(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0

        start, length = 0, 0
        for i in xrange(len(s)):
            if i - length - 1 >= 0 and self.isPalindrome(s[i - length - 1:i + 1]):
                start = i - length - 1
                length += 2
            elif self.isPalindrome(s[i - length:i + 1]):
                start = i - length
                length += 1
        return s[start:start + length]

    def isPalindrome(self, s):
        return s == s[::-1]

sol = Solution_self()
print sol.longestPalindrome('abccba')
