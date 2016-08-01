# no Liana solution


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_of_two = 0
        for n in nums:
            xor_of_two ^= n

        mask = 1
        while xor_of_two & mask == 0:
            mask <<= 1

        first, second = 0, 0
        for n in nums:
            if n & mask:
                first ^= n
            else:
                second ^= n
        return [first, second]

sol = Solution()
print sol.singleNumber([1, 2, 1, 3, 2, 5])
