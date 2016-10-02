def quick_sort(nums):
    quick_sort_helper(nums, 0, len(nums) - 1)


def quick_sort_helper(nums, first, last):
    if first < last:
        # set first num as pivot, then put all nums <= pivot
        # to left, all nums >= pivot to right, and pivot in
        # between, so pivot is in the right position
        pivot = nums[first]
        leftmark = first + 1
        rightmark = last

        done = False
        while not done:
            # increment leftmark to the fist num greater than pivot
            while leftmark <= rightmark and nums[leftmark] <= pivot:
                leftmark += 1

            # at last loop this will point rightmark right to the last
            # num of smaller part, this is why we can exchange pivot
            # and num pointed by rightmark, because it is smaller than
            # pivot anyway
            while leftmark <= rightmark and nums[rightmark] >= pivot:
                rightmark -= 1

            if rightmark < leftmark:
                done = True
            else:
                nums[leftmark], nums[rightmark] = nums[rightmark], nums[leftmark]

        nums[first], nums[rightmark] = nums[rightmark], nums[first]

        # recursively call itself for left part and right part
        quick_sort_helper(nums, first, rightmark - 1)
        quick_sort_helper(nums, rightmark + 1, last)

test_nums = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
quick_sort(test_nums)
print test_nums
