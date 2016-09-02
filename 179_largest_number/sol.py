# no Liana solution


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums or len(nums) == 0:
            return "0"

        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp(y + x, x + y))
        result = ''.join(nums).lstrip('0')
        return result if len(result) > 0 else "0"
