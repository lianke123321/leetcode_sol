# no Liana solution


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i, count = 0, 0
        for i in xrange(len(data)):
            binary = format(data[i], '08b')
            if count:
                if binary.startswith('10'):
                    count -= 1
                else:
                    return False
            else:
                idx = binary.find('0')
                if binary.startswith('10') or idx < 0 or idx > 4:
                    return False
                count = idx - 1 if idx > 0 else 0
        return count == 0

sol = Solution()
print sol.validUtf8([145])
