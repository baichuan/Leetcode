class NumArray(object):

    def __init__(self, nums):

        """
        initialize your data structure here.
        :type nums: List[int]
        """

        self.sumList = [];
        self.sum = 0;

        for i in range(0, len(nums)):
            self.sum = self.sum + nums[i];
            self.sumList.append(self.sum);

    def sumRange(self, i, j):

        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        if i == 0:
            return self.sumList[j];

        else:
            return self.sumList[j] - self.sumList[i-1];


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
