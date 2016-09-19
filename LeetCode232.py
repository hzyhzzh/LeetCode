class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.input = []
        self.output = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.input.append(x)
        self.output = self.input[::-1]

    def pop(self):
        """
        :rtype: nothing
        """
        self.output.pop()
        self.input = self.output[::-1]


    def peek(self):
        """
        :rtype: int
        """
        return self.output[-1]


    def empty(self):
        """
        :rtype: bool
        """
        if len(self.input):
            return False
        else:
            return True
