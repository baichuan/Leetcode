class Solution(object):

    def twoSum(self, numbers, target):

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # solve it using two pointers

        l = 0;
        r = len(numbers) - 1;

        while l < r:

            sum = numbers[l] +  numbers[r];

            if sum == target:
                return [l + 1, r + 1];

            elif sum < target:

                l = l + 1;

            else:

                r = r - 1;


class Solution(object):

    def twoSum(self, numbers, target):

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {};

        for i in range(0, len(numbers)):

            if target - numbers[i] in dict:
                return [dict[target - numbers[i]] + 1, i + 1];

            dict[numbers[i]] = i;
