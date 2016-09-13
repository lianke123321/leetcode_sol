# no Liana solution


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    return 4


class Solution(object):
    def __init__(self):
        from collections import deque
        self.cache = deque()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx, buf4 = 0, [''] * 4
        while True:
            c = read4(buf4)
            self.cache.extend(buf4[:c])
            while idx < n and len(self.cache) > 0:
                buf[idx] = self.cache.popleft()
                idx += 1
            if idx == n or c < 4:
                break
        return idx

