# no Liana solution

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            if numbers[lo] + numbers[hi] > target:
                hi -= 1
            elif numbers[lo] + numbers[hi] == target:
                return [lo + 1, hi + 1]
            else:
                lo += 1

        return [-1, -1]
