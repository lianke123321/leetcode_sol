# no Liana solution


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.cache = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            curr_list, idx = self.cache[-1]
            self.cache[-1][1] += 1
            return curr_list[idx].getInteger()
        else:
            return None

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.cache:
            curr_list, idx = self.cache[-1]
            if idx == len(curr_list):
                self.cache.pop()
                continue
            if curr_list[idx].isInteger():
                return True
            self.cache[-1][1] += 1
            self.cache.append([curr_list[idx].getList(), 0])
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
