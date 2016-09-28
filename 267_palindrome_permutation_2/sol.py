# no Liana solution


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        from collections import Counter
        c = Counter(s)

        has_odd, odd_letter = False, None
        for l in c:
            if c[l] % 2 != 0:
                if has_odd:
                    return result
                else:
                    has_odd = True
                    odd_letter = l

        if has_odd:
            stack = [''] * (len(s) / 2) + [odd_letter] + [''] * (len(s) / 2)
            c[odd_letter] -= 1
        else:
            stack = [''] * len(s)
        self.dfs(stack, 0, c, result)
        return result

    def dfs(self, stack, start, counter, result):
        if start >= len(stack) / 2:
            result.append(''.join(stack))
        else:
            for letter in counter:
                if counter[letter] > 0:
                    stack[start] = stack[len(stack) - start - 1] = letter
                    counter[letter] -= 2
                    self.dfs(stack, start + 1, counter, result)
                    counter[letter] += 2

sol = Solution()
print sol.generatePalindromes('as')
