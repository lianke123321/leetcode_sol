def radix_sort(nums):
    radix, reach_max, placement = 10, False, 1
    while not reach_max:
        reach_max = True
        buckets = [list() for _ in xrange(radix)]

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

test_radix_sort = [3221, 1, 10, 9680, 577, 9420, 7, 5622, 4793, 2030, 3138, 82, 2599, 743, 4127]
radix_sort(test_radix_sort)
print test_radix_sort
