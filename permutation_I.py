class Solution(object):

    def permute(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

	# time complexity = O(n!) and space complexity = O(n!)

	# keep track of permutation of [1,2,3]        

	# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]

        res = [];
        temp_list = [];
        
        if nums == []:
            return [];
            
        self.helper(res, temp_list, nums);
        
        return res;
        

    def helper(self, res, temp_list, nums):
        
        if len(temp_list) == len(nums):
            
            copy_list = list(temp_list);
            res.append(copy_list);
            return;

        else:
            
            for i in range(0, len(nums)):
            
                if nums[i] in temp_list:
                    continue;
                
                else:
                    
                    temp_list.append(nums[i]);
                    self.helper(res, temp_list, nums);
                    temp_list.remove(temp_list[len(temp_list) - 1]);
