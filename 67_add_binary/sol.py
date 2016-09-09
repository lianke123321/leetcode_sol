class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        result = ''
        temp = 0
        while (i >= 0 or j >= 0 or temp == 1):
            if i >= 0:
                temp += int(a[i])
                i -= 1
            if j >= 0:
                temp += int(b[j])
                j -= 1
            result = str(temp % 2) + result
            temp /= 2
        return result

    def addBinary_self(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        result, tmp = '', 0
        while i >= 0 or j >= 0 or tmp > 0:
            if i >= 0:
                tmp += int(a[i])
                i -= 1
            if j >= 0:
                tmp += int(b[j])
                j -= 1
            result = str(tmp & 1) + result
            tmp >>= 1
        return result if len(result) > 0 else '0'

sol = Solution()
print sol.addBinary_self('0', '1')
