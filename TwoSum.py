__author__ = 'Adrian'


# failed version one
class Solution_1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        possible_nums = []
        for i in range(0, len(nums)):
            if nums[i] >= target:
                continue
            else:
                if len(possible_nums) == 0:
                    possible_nums.append(i)
                else:
                    for index in possible_nums:
                        if nums[index] + nums[i] == target:
                            return [index, i]
                    possible_nums.append(i)


# failed version two
class Solution_2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            if nums[i] >= target:
                continue
            else:
                want_num = target - nums[i]
                if want_num in nums and nums.index(want_num) != i:
                    return [i, nums.index(want_num)]


# failed version three
class Solution_3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            if nums[i] >= target:
                continue
            else:
                want_num = target - nums[i]
                if want_num != nums[i] and want_num in nums:
                    return [i, nums.index(want_num)]


# failed version four
class Solution_4(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.iteration(nums, target, target)

    def iteration(self, nums, target, sub_target):
        if sub_target/2 == 0:
            return None
        else:
            want_num = sub_target/2

            if want_num == target - want_num:
                want_num -= 1

            if want_num in nums and target-want_num in nums:
                index_1 = min(nums.index(want_num), nums.index(target-want_num)) + 1
                index_2 = max(nums.index(want_num), nums.index(target-want_num)) + 1
                return [index_1, index_2]
            else:
                return self.iteration(nums, target, want_num)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        set_nums = set(nums)
        if len(nums) == len(set_nums):
            for num in set_nums:
                want_num = target - num
                if want_num != num and want_num in set_nums:
                    index_1 = min(nums.index(num)+1, nums.index(want_num)+1)
                    index_2 = max(nums.index(num)+1, nums.index(want_num)+1)
                    return [index_1, index_2]
        else:
            duplicates = list_duplicates(nums)
            for num in duplicates:
                if 2*num == target:
                    indices = list_duplicates_of(nums, num)
                    index_1 = min(indices[0]+1, indices[1]+1)
                    index_2 = max(indices[0]+1, indices[1]+1)
                    return [index_1, index_2]
            for num in set_nums:
                want_num = target - num
                if want_num != num and want_num in set_nums:
                    index_1 = min(nums.index(num)+1, nums.index(want_num)+1)
                    index_2 = max(nums.index(num)+1, nums.index(want_num)+1)
                    return [index_1, index_2]


def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    # turn the set into a list (as requested)
    return list(seen_twice)


def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

s = Solution()
nums = [-1, -2, -3, -4, -5]
print s.twoSum(nums, -8)
