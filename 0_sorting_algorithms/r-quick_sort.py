def r_quick_sort(nums):
    r_quick_sort_helper(nums, 0, len(nums) - 1)


def r_quick_sort_helper(nums, first, last):
    if first < last:
        pivot = nums[first]
        swap_pos = first + 1

        for i in range(first + 1, last + 1):
            if nums[i] <= pivot:
                nums[swap_pos], nums[i] = nums[i], nums[swap_pos]
                swap_pos += 1

        nums[first], nums[swap_pos - 1] = nums[swap_pos - 1], nums[first]

        r_quick_sort_helper(nums, first, swap_pos - 2)
        r_quick_sort_helper(nums, swap_pos, last)

test_nums = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
r_quick_sort(test_nums)
print test_nums
