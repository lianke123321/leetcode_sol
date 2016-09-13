class Solution(object):
    def getPivot(self, nums, lo, hi):
        if lo == hi:
            return lo
        i = lo
        j = i + 1
        while j <= hi:
            if nums[j] > nums[lo]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        nums[lo], nums[i] = nums[i], nums[lo]
        return i

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) < k:
            return 0
        lo = 0
        hi = len(nums) - 1
        pivot = self.getPivot(nums, lo ,hi)
        while pivot + 1 != k:
            if pivot < k:
                lo = pivot + 1
            if pivot > k:
                hi = pivot - 1
            pivot = self.getPivot(nums, lo, hi)
        return nums[pivot]


class Solution_self(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.findKthSmallest(nums, len(nums) - k + 1)

    def findKthSmallest(self, nums, k):
        idx = self.quick_sort_helper(nums)
        if idx == k - 1:
            return nums[idx]
        elif idx > k - 1:
            return self.findKthSmallest(nums[:idx], k)
        else:
            return self.findKthSmallest(nums[idx + 1:], k - idx - 1)

    def quick_sort_helper(self, nums):
        pivot, leftmark, rightmark, done = nums[0], 1, len(nums) - 1, False
        while not done:
            while leftmark <= rightmark and nums[leftmark] <= pivot:
                leftmark += 1

            while leftmark <= rightmark and nums[rightmark] >= pivot:
                rightmark -= 1

            if rightmark < leftmark:
                done = True
            else:
                nums[leftmark], nums[rightmark] = nums[rightmark], nums[leftmark]

        nums[0], nums[rightmark] = nums[rightmark], nums[0]
        return rightmark

sol = Solution_self()
print sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
