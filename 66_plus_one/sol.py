class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        increment = 1
        while i >= 0:
            temp = digits[i] + increment
            digits[i] = temp % 10
            increment = temp / 10
            i -= 1
        if increment == 1:
            digits.insert(0, 1)
        return digits

    def plusOne_self(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(xrange(len(digits))):
            carry += digits[i]
            digits[i] = carry % 10
            carry /= 10
            if carry == 0:
                break
        return [carry] + digits if carry else digits
