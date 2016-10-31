class Queue(object):

    def __init__(self):

        """
        initialize your data structure here.
        """

        self.stack = [];

    def push(self, x):

        """
        :type x: int
        :rtype: nothing
        """

        temp = [];

        while self.stack:
            temp.append(self.stack.pop());

        temp.append(x);

        while temp:
            self.stack.append(temp.pop());

            
    def pop(self):

        """
        :rtype: nothing
        """

        self.stack.pop();


    def peek(self):

        """
        :rtype: int
        """

        return self.stack[-1];

        
    def empty(self):

        """
        :rtype: bool
        """

        return len(self.stack) == 0;
