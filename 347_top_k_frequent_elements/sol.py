# no Liana solution


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq
        c = Counter(nums)
        return heapq.nlargest(k, c, c.get)

sol = Solution()
print sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
