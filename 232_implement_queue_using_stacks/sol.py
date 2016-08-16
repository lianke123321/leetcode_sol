class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        self.first = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.queue:
            self.first = x
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.remove(self.first)
        if self.queue:
            self.first = self.queue[0]

    def peek(self):
        """
        :rtype: int
        """
        return self.first

    def empty(self):
        """
        :rtype: bool
        """
        if not self.queue:
            return True
        else:
            return False


class Queue_self(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.in_stack, self.out_stack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        return self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        last = self.out_stack.pop()
        self.out_stack.append(last)
        return last

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack

    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
