# no Liana solution


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        hashmap = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        center, res, stack = {'0', '1', '8'}, [], ['a'] * n
        if n == 0:
            return res

        def dfs(i):
            if i == n / 2:
                res.append(''.join(stack))
                return

            for k in hashmap:
                if i > 0 or (i == 0 and k != '0'):
                    stack[i], stack[n - i - 1] = k, hashmap[k]
                    dfs(i + 1)

        if n % 2:
            for c in center:
                stack[n / 2] = c
                dfs(0)
        else:
            dfs(0)
        return res

sol = Solution()
print sol.findStrobogrammatic(3)
