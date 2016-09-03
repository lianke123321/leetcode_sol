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
        longest, l_to_idx, start, p = 0, {}, 0, 0
        while p < len(s):
            if s[p] in l_to_idx:
                longest = max(longest, p - start)
                start = max(start, l_to_idx[s[p]] + 1)
            l_to_idx[s[p]] = p
            p += 1
        return max(longest, p - start)

sol = Solution()
print sol.lengthOfLongestSubstring_self('abcdabaa')
