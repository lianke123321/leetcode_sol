# no Liana solution


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = None, None
        for n in nums:
            if first is None or n < first:
                first = n

            if (second is None and n > first) or (second is not None and first < n < second):
                second = n

            if second is not None and n > second:
                return True
        return False

sol = Solution()
print sol.increasingTriplet([2, 4, -2, -3])
