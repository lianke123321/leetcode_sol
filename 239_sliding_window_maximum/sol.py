# no Liana solution
from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q, res = deque(), []
        for idx, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(idx)
            if q[0] == idx - k:
                q.popleft()
            if idx >= k - 1:
                res.append(nums[q[0]])
        return res

sol = Solution()
print sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
