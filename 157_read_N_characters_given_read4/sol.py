# no Liana solution


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx, buf4 = 0, [""] * 4
        while n > 0:
            count = read4(buf4)
            for i in xrange(min(count, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
            if count < 4:
                break
        return idx
