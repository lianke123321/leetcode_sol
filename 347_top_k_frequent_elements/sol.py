# no Liana solution


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        c = Counter(nums)
        return sorted(c, key=c.get, reverse=True)[:k]

sol = Solution()
print sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
