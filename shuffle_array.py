import random;
class Solution(object):
    def __init__(self, nums):

        """
        :type nums: List[int]
        :type size: int
        """

        self.initial_list = nums;

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """

        return self.initial_list;

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        copy_list = list(self.initial_list);
        length = len(copy_list);
        for i in range(0, length):
            rand_index = random.randint(i, length-1);
            copy_list[i], copy_list[rand_index] = copy_list[rand_index], copy_list[i];

        return copy_list;

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
