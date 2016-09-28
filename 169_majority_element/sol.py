class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                major = nums[i]
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major

    def majorityElement_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count = nums[0], 1
        for i in xrange(1, len(nums)):
            if count == 0:
                result = nums[i]
                count += 1
            elif result == nums[i]:
                count += 1
            else:
                count -= 1
        return result

    def majorityElement_bit_manipulation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit_counter = [0] * 32
        for n in nums:
            binary = bin(n)[2:]
            j = 0
            for i in reversed(xrange(len(binary))):
                if binary[i] == '1':
                    bit_counter[j] += 1
                j += 1

        res = ''
        for c in bit_counter:
            res = '1' + res if c > len(nums) / 2 else '0' + res
        return int(res.lstrip('0'), 2)

sol = Solution()
print sol.majorityElement_bit_manipulation([1, 3, 5, 5, 5])
