# no Liana solution


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    return True


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in xrange(n):
            if knows(candidate, i):
                candidate = i
        for i in xrange(n):
            if not knows(i, candidate) or (i != candidate and knows(candidate, i)):
                return -1
        return candidate
