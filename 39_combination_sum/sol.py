class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        stack = [(0, 0, [])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target:
                result.append(res)
            for i in range(start, len(candidates)):
                t = total + candidates[i]
                if t > target:
                    break
                stack.append((t, i, res + [candidates[i]]))
        return result


class Solution_self(object):
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.dfs([], candidates, target)
        return self.result

    def dfs(self, stack, candidates, target):
        if target == 0:
            self.result.append(stack)
        else:
            for i in xrange(len(candidates)):
                if candidates[i] > target:
                    break
                self.dfs(stack + [candidates[i]], candidates[i:], target - candidates[i])
