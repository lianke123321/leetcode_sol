class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        pos = len(result) - 1
        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                result[tempPos] += int(n1) * int(n2)
                result[tempPos - 1] += result[tempPos] / 10
                result[tempPos] %= 10
                tempPos -= 1
            pos -= 1
        pt = 0
        while pt < len(result) - 1 and result[pt] == 0:
            pt += 1
        return ''.join(map(str, result[pt:]))

    def multiply_self(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        digits = [0] * (len(num1) + len(num2))
        for i in reversed(xrange(len(num1))):
            for j in reversed(xrange(len(num2))):
                tmp = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                tmp += digits[p2]
                digits[p1] += tmp / 10
                digits[p2] = tmp % 10
        start, ret = len(digits) - 1, ''
        for i in xrange(len(digits)):
            if digits[i] != 0:
                start = i
                break
        return ''.join(str(x) for x in digits[start:])

sol = Solution()
print sol.multiply_self('0', '0')
