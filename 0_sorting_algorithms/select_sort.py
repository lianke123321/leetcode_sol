def select_sort(nums):
    first_unsorted = 0
    while first_unsorted < len(nums):
        found = False
        min_num = nums[first_unsorted]
        min_index = first_unsorted
        for i in range(first_unsorted + 1, len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
                min_index = i
                found = True
        if found:
            nums[first_unsorted], nums[min_index] = nums[min_index], nums[first_unsorted]
        first_unsorted += 1
    return nums

test_nums = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print select_sort(test_nums)
