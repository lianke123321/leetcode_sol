# no Liana solution


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count, stack, visited = [0] * 26, [], [False] * 26
        for x in s: count[ord(x) - ord('a')] += 1

        for x in s:
            count[ord(x) - ord('a')] -= 1
            if visited[ord(x) - ord('a')] or (stack and stack[-1] == x):
                continue

            while stack and ord(x) < ord(stack[-1]) and count[ord(stack[-1]) - ord('a')] > 0:
                visited[ord(stack[-1]) - ord('a')] = False
                stack.pop()
            stack.append(x)
            visited[ord(x) - ord('a')] = True
        return ''.join(stack)

sol = Solution()
print sol.removeDuplicateLetters("cbacdcbc")
