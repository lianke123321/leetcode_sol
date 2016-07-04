# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        while lo < hi:
            mid = lo + (hi - lo) / 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1  # Only one call to API
        return lo  # Because there will alway be a bad version, return lower here

    def firstBadVersion_self(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low < high:
            mid = (low + high) / 2
            if isBadVersion(mid):
                high = mid
            else:
                # we want low to be the first bad version, and we alread know that mid
                # is not bad here, so set low to mid + 1 could save some calls to API
                low = mid + 1
        return low
