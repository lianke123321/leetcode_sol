class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            elif hashMap[nums[i]] < i - k:
                hashMap[nums[i]] = i
            else:
                return True
        return False

    def containsNearbyDuplicate_self(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = dict()
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                if abs(i - hash_map[nums[i]]) <= k:
                    return True
                hash_map[nums[i]] = i
        return False
