class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        map = {}
        left = 0
        right = 0
        while right < len(s):
            if s[right] in map:
                left = max(left, map[s[right]] + 1)
            map[s[right]] = right
            longest = max(longest, right - left + 1)
            right += 1
        return longest

    def lengthOfLongestSubstring_self(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        result = 0
        ls = set()
        start = 0
        i = 0
        while i < len(s):
            if s[i] not in ls:
                ls.add(s[i])
                i += 1
            else:
                length = i - start
                if length > result:
                    result = length
                ls.remove(s[start])
                start += 1
        return result

sol = Solution()
print sol.lengthOfLongestSubstring_self('abcdabaa')
