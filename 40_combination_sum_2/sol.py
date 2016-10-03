class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        stack = [(0, -1, [])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target and res not in result:
                result.append(res)
            for i in range(start + 1, len(candidates)):
                t = total + candidates[i]
                if t > target:
                    break
                stack.append((t, i, res + [candidates[i]]))
        return result


class Solution_self(object):
    def __init__(self):
        self.result = set()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.dfs([], candidates, target)
        return [list(l) for l in self.result]

    def dfs(self, stack, candidates, target):
        if target == 0:
            self.result.add(tuple(stack))
        else:
            for i in xrange(len(candidates)):
                if candidates[i] > target:
                    break
                self.dfs(stack + [candidates[i]], candidates[i + 1:], target - candidates[i])

sol = Solution_self()
print sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
