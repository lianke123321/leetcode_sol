def insert_sort(nums):
    last_sorted = 0
    while last_sorted < len(nums) - 1:
        new_num = nums[last_sorted + 1]
        i = last_sorted
        while i >= 0:
            if nums[i] > new_num:
                nums[i+1] = nums[i]
            else:
                nums[i+1] = new_num
                break

            # if we reached first num
            if i == 0:
                nums[i] = new_num
            i -= 1
        last_sorted += 1
    return nums

test_nums = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print insert_sort(test_nums)
