class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)  # Could be negative if min value needs to change
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.stack:
            return None
        temp = self.stack.pop()
        if temp < 0:
            self.min -= temp  # If negative, increase the min value

    def top(self):
        """
        :rtype: int
        """
        temp = self.stack[-1]
        if temp > 0:
            return temp + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


class MinStack_self(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        tmp = self.stack.pop()
        if tmp < 0:
            self.min -= tmp

    def top(self):
        """
        :rtype: int
        """
        tmp = self.stack.pop()
        self.stack.append(tmp)
        if tmp >= 0:
            return self.min + tmp
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
