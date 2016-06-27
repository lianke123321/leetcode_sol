__author__ = 'Adrian'

import time

from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        set_results = set()
        final_results = []
        # dict_nums = Counter(nums)
        dict_nums = {}
        for num in nums:
            if num not in dict_nums:
                dict_nums[num] = nums.count(num)

        for i in range(0, len(nums)):
            for m in range(i+1, len(nums)):
                num_1 = nums[i]
                num_2 = nums[m]
                want_num = - num_1 - num_2

                dict_nums[num_1] -= 1
                dict_nums[num_2] -= 1

                if want_num in dict_nums and dict_nums[want_num] > 0:
                    new_triplet = tuple(sorted([num_1, num_2, want_num]))
                    if new_triplet not in set_results:
                        set_results.add(new_triplet)

                dict_nums[num_1] += 1
                dict_nums[num_2] += 1

        for triplet in set_results:
            final_results.append(list(triplet))

        return final_results

s = Solution()
nums = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
start_time = time.time()
print s.threeSum(nums)
print time.time() - start_time
