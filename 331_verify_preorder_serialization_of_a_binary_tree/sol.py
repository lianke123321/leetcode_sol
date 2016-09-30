# no Liana solution


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        diff = 1
        for c in preorder.split(','):
            diff -= 1
            if diff < 0:
                return False
            if c != '#':
                diff += 2
        return diff == 0
