# no Liana solution

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(numbers) - 1
        if numbers[lo] > target:
            return [-1, -1]

        while lo < hi:
            if numbers[lo] + numbers[hi] > target:
                hi -= 1
            elif numbers[lo] + numbers[hi] == target:
                return [lo + 1, hi + 1]
            else:
                lo += 1
        return [-1, -1]

sol = Solution()
print sol.twoSum([-3, 3, 4, 90], 0)
