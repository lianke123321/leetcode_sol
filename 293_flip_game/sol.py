# no Liana solution


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res, p = [], 0
        while p < len(s) - 1:
            if s[p] == '+' and s[p + 1] == '+':
                res.append(s[:p] + '--' + s[p + 2:])
            p += 1
        return res

sol = Solution()
print sol.generatePossibleNextMoves('++++')
