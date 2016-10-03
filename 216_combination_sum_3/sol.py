class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = [i for i in range(1, 10)]
        target = n

        stack = [(0, -1, [])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target and len(res) == k:
                result.append(res)
            for i in range(start + 1, len(candidates)):
                t = total + candidates[i]
                if t > target:
                    break
                stack.append((t, i, res + [candidates[i]]))
        return result


class Solution_self(object):
    def __init__(self):
        self.result = []

    def combinationSum3(self, k, n):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = range(1, 10)
        target = n
        self.dfs([], candidates, target, k)
        return self.result

    def dfs(self, stack, candidates, target, k):
        if target == 0:
            if len(stack) == k:
                self.result.append(stack)
        elif len(stack) >= k:
            return
        else:
            for i in xrange(len(candidates)):
                if candidates[i] > target:
                    break
                self.dfs(stack + [candidates[i]], candidates[i + 1:], target - candidates[i], k)

sol = Solution_self()
print sol.combinationSum3(3, 9)
