class Solution(object):

    def __init__(self, nums):

        """
        :type nums: List[int]

        :type numsSize: int

        """

        self.dict = {};

        for i in range(0, len(nums)):

            if nums[i] not in self.dict:
                
                self.dict[nums[i]] = [i];

            else:

                tempList = self.dict[nums[i]];
                tempList.append(i);
                self.dict[nums[i]] = tempList;


    def pick(self, target):

        """
        :type target: int
        :rtype: int
        """

        index_list = self.dict[target];
        return random.choice(index_list);

        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


# reservior sampling

class Solution(object):

    def __init__(self, nums):

        """
        :type nums: List[int]
        :type numsSize: int
        """

        self.copy_nums = nums;


    def pick(self, target):

        """
        :type target: int
        :rtype: int
        """

        result_index = -1;
        count = 0;
        
        for i in range(0, len(self.copy_nums)):

            if self.copy_nums[i] == target:

                count += 1;

                if random.randint(0, count - 1) == 0:
                    result = i;

        return result;


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
