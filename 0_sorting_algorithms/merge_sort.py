def merge_sort(nums):
    if len(nums) <= 1:
        return nums

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

test_nums = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print merge_sort(test_nums)
