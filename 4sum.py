class Solution(object):

    def fourSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # consider the base case first
        dict = {};
        nums.sort();
        if len(nums) < 4:
            return [];

        # build a dict first two elements as key and their corresponding index as value

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] not in dict:
                    tuple_list = [];
                    tuple_list.append((i, j));
                    dict[nums[i] + nums[j]] = tuple_list;

                else:
                    tuple_list = dict[nums[i] + nums[j]];
                    tuple_list.append((i, j));
                    dict[nums[i] + nums[j]] = tuple_list;

        result_list = [];
        for pos in range(0, len(nums)):
            for inpos in range(pos+1, len(nums) - 2):
                T = target - nums[pos] - nums[inpos];
                if T in dict:
                    for k in range(0, len(dict[T])):
                        if dict[T][k][0] > inpos:
                            result_list.append(sorted((nums[pos], nums[inpos], nums[dict[T][k][0]], nums[dict[T][k][1]])));

        b = list()
        for sublist in result_list:
            if sublist not in b:
                b.append(sublist)
        return b;
