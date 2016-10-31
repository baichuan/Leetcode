import random;

class RandomizedSet(object):

    def __init__(self):

        """
        Initialize your data structure here.
        """
        self.random_set = set();

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.random_set:
            self.random_set.add(val);
            return True;
        else:
            return False;

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.random_set:
            self.random_set.remove(val);
            return True;
        else:
            return False;

    def getRandom(self):

        """
        Get a random element from the set.
        :rtype: int
        """
        rand_index = random.randint(0, len(self.random_set)-1);
        return list(self.random_set)[rand_index];


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
