# no Liana solution


from collections import deque


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result, visited, queue, found = [], {s}, deque(), False
        queue.append(s)
        while queue:
            candidate = queue.pop()
            if self.is_valid(candidate):
                result.append(candidate)
                found = True

            if found:
                continue

            for i in xrange(len(candidate)):
                if candidate[i] == '(' or candidate[i] == ')':
                    child = candidate[:i] + candidate[i + 1:]
                    if child not in visited:
                        queue.appendleft(child)
                        visited.add(child)
        return result

    def is_valid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                if count == 0:
                    return False
                count -= 1
        return count == 0

sol = Solution()
print sol.removeInvalidParentheses('()())()')
