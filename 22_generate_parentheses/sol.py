class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # p is the parenthesis-string built so far,
        # left and right tell the number of left and right parentheses still to add,
        # and result collects the parentheses.
        def generate(p, left, right, result=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                result.append(p)
            return result

        return generate('', n, n)


class Solution_self(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 0:
            return res

        self.helper(n, 0, '', res)
        return res

    def helper(self, n, count, cache, res):
        if n == 0:
            res.append(cache + ')' * count)
            return

        if n > 0:
            self.helper(n - 1, count + 1, cache + '(', res)
        if count > 0:
            self.helper(n, count - 1, cache + ')', res)

sol = Solution_self()
print sol.generateParenthesis(3)
