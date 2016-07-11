# no Liana solution


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        hashmap = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        new_num = ''
        for i in range(len(num) - 1, -1, -1):
            if num[i] not in hashmap:
                return False
            else:
                new_num += hashmap[num[i]]

        return new_num == num
