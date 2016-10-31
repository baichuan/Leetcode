class Solution(object):

# Example 1: 
# input is 14532 and then we find partition is 4. Scan the array from the end, 5 is the first number which is larger than 4, switch them, becoming 15432, then reverse the 432 => 234, so final result is 15234
# Example 2: If input is 54321, then result is 12345

    def nextPermutation(self, nums):

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

	# example: 158476531 => 158513467
        partition = -1

        for i in range(len(nums)-2, -1, -1):

            if nums[i] < nums[i+1]:

                # 从后向前找到第一个升序对，并让partition等于升序对中较小的
                partition = i
                break

        if partition == -1:
            # 没找到升序对 e.g. 54321 --> 12345
            nums.reverse()

        else:
            for i in range(len(nums)-1, partition, -1):
                # 交换partition和升序对后面比partition更大的数 如14532 -> 15432
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break

        # 将partition后面的数字逆向排序。由于找到的partition是从后向前的第一个升序对，所以可以放心partition后面一定都是降序的
        # 所以逆向排序后可以得到一个新的刚好大于之前permutation的next permutation
        # 比如此时14532已经变为15432，则再将5（此时partition已经是5了）后面的432逆序排列得到234.则最终的数字变为15234
            nums[partition+1:len(nums)] = nums[partition+1:len(nums)][::-1]
