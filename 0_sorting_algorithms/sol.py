def bubble_sort(nums):
    last_unsorted = len(nums) - 1
    while True:
        swapped = False
        for i in range(last_unsorted):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        last_unsorted -= 1
        if not swapped or last_unsorted == 0:
            return nums


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


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        sorted_1 = merge_sort(nums[:len(nums)/2])
        sorted_2 = merge_sort(nums[len(nums) / 2:])
        m = len(sorted_1)
        n = len(sorted_2)
        result = [0] * (m + n)
        while m > 0 and n > 0:
            if sorted_1[m - 1] >= sorted_2[n - 1]:
                result[m + n - 1] = sorted_1[m - 1]
                m -= 1
            else:
                result[m + n - 1] = sorted_2[n - 1]
                n -= 1

        if m > 0:
            result[:m] = sorted_1[:m]
        if n > 0:
            result[:n] = sorted_2[:n]

        return result


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


def count_sort(nums, k):
    counter = [0] * (k + 1)
    for num in nums:
        counter[num] += 1

    p = 0
    for i in range(len(counter)):
        while counter[i] > 0:
            nums[p] = i
            p += 1
            counter[i] -= 1


def radix_sort(nums):
    radix = 10
    reach_max = False
    placement = 1

    while not reach_max:
        reach_max = True
        buckets = [list() for _ in range(radix)]

        for num in nums:
            tmp = num / placement
            buckets[tmp % radix].append(num)
            if reach_max and tmp > 0:
                reach_max = False

        p = 0
        for b in range(radix):
            for num in buckets[b]:
                nums[p] = num
                p += 1

        # move to next digit
        placement *= radix


# test_nums = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
# print bubble_sort(test_nums)

# print select_sort(test_nums)

# print insert_sort(test_nums)

# print merge_sort(test_nums)

# quick_sort(test_nums)
# print test_nums

# r_quick_sort(test_nums)
# print test_nums

# test_count_sort = [2, 1, 3, 6, 2, 1, 9, 4, 9, 5]
# count_sort(test_count_sort, 9)
# print test_count_sort

# test_radix_sort = [3221, 1, 10, 9680, 577, 9420, 7, 5622, 4793, 2030, 3138, 82, 2599, 743, 4127]
# radix_sort(test_radix_sort)
# print test_radix_sort
