# no Liana solution


class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.children = []


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.root = self.build(0, len(nums) - 1, nums)

    def build(self, start, end, nums):
        if start > end:
            return

        root = SegmentTreeNode(0, start, end)
        if start != end:
            mid = start + end >> 1
            root.children = filter(None, [self.build(start, end, nums)
                                          for start, end in (start, mid), (mid + 1, end)])
            root.val = sum([c.val for c in root.children])
        else:
            root.val = nums[start]
        return root

    def update(self, i, val, root=None):
        """
        :type i: int
        :type val: int
        :type root: SegmentTreeNode
        :rtype: int
        """
        root = root or self.root
        if i == root.start == root.end:
            root.val = val
        elif root.start <= i <= root.end:
            root.val = sum([self.update(i, val, c) for c in root.children])
        return root.val

    def sumRange(self, i, j, root=None):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :type root: SegmentTreeNode
        :rtype: int
        """
        root = root or self.root
        if j < root.start or i > root.end:
            return 0
        if i <= root.start and j >= root.end:
            return root.val
        return sum([self.sumRange(i, j, c) for c in root.children])


# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1, 3, 5])
print numArray.sumRange(0, 1)
numArray.update(1, 10)
print numArray.sumRange(1, 2)
