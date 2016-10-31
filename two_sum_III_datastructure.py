# follow-up: if call find() function lots of time, how to optimize ? 
# We can store all the find result. If curr search target is same as previous target, directly return previous target result

class TwoSum(object):


    def __init__(self):

        """
        initialize your data structure here
        """

        self.dict = {};

    def add(self, number):

        """
        Add the number to an internal data structure.
        :rtype: nothing
        """

        if number not in self.dict:
            self.dict[number] = 1;

        else:
            self.dict[number] += 1;


    def find(self, value):

        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        dict = self.dict;
        for k in dict:
            j = value - k;
            if (k == j and dict[k] > 1) or (k != j and j in dict):
                return True;
               
        return False;


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)

class TwoSum(object):

    def __init__(self):

        """
        initialize your data structure here
        """

        self.list = [];


    def add(self, number):

        """
        Add the number to an internal data structure.
        :rtype: nothing
        """

        self.list.append(number);


    def find(self, value):

        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        list = self.list;
        self.hashset = set();
        
        for i in range(0, len(list)):
            
            if value - list[i] in self.hashset:
                return True;
                
            self.hashset.add(list[i]);
            
        return False;


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
