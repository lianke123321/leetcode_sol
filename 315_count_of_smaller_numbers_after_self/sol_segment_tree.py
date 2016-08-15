# no Liana solution


class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.children = []


class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, start, end):
        if start > end:
            return

        root = SegmentTreeNode(0, start, end)
        if start != end:
            mid = start + end >> 1
            root.children = filter(None, [self.build(start, end) for start, end in (start, mid), (mid + 1, end)])
        return root

    def update(self, i, val, root=None):
        root = root or self.root
        if i == root.start == root.end:
            root.val += val
        elif root.start <= i <= root.end:
            root.val = sum([self.update(i, val, c) for c in root.children])
        return root.val

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0
        if start <= root.start and end >= root.end:
            return root.val
        return sum([self.sum(start, end, c) for c in root.children])


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashtable = {v: i for i, v in enumerate(sorted(set(nums)))}
        tree, r = SegmentTree(len(hashtable)), []

        for i in reversed(xrange(len(nums))):
            r.append(tree.sum(0, hashtable[nums[i]] - 1))
            tree.update(hashtable[nums[i]], 1)
        return r[::-1]

sol = Solution()
print sol.countSmaller([5, 2, 6, 1])
