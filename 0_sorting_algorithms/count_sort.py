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

test_count_sort = [2, 1, 3, 6, 2, 1, 9, 4, 9, 5]
count_sort(test_count_sort, 9)
print test_count_sort
