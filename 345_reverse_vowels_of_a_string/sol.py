# no Liana solution


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(list('aeiouAEIOU'))
        start, end, res = 0, len(s) - 1, list(s)
        while start < end:
            while start < end and res[start] not in vowels:
                start += 1
            while start < end and res[end] not in vowels:
                end -= 1
            if start < end:
                res[start], res[end] = res[end], res[start]
                start += 1
                end -= 1
        return ''.join(res)

sol = Solution()
print sol.reverseVowels('hello')
