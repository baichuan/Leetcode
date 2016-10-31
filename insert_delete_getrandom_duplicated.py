import random;
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomList = [];


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.randomList:
            self.randomList.append(val);
            return True;
        else:
            self.randomList.append(val);
            return False;

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.randomList:
            self.randomList.remove(val);
            return True;
        else:
            return False;

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        rand_index = random.randint(0, len(self.randomList)-1);
        return self.randomList[rand_index];

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
