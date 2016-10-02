def bubble_sort(nums):
    last_unsorted = len(nums) - 1
    while True:
        swapped = False
        for i in xrange(last_unsorted):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped, last_unsorted = True, i
        if not swapped:
            return nums

test_nums = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print bubble_sort(test_nums)
