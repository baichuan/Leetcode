class Solution(object):

    def permuteUnique(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # if found duplicated elements, only previous one is used, then we can use the current element
        
        res = [];
        nums.sort();
        temp_list = [];

        bool_list = [False] * len(nums);

        self.helper(res, temp_list, nums, bool_list);
        
        return res;
        
    def helper(self, res, temp_list, nums, bool_list):
        
        if len(temp_list) == len(nums):
            
            copy_list = list(temp_list);
            res.append(copy_list);
            return;
            
        else:
            for i in range(0, len(nums)):
                
                if bool_list[i] == True or (i > 0 and nums[i - 1] == nums[i] and bool_list[i - 1] == False):
                    continue;
                    
                bool_list[i] = True;
                temp_list.append(nums[i]);
                self.helper(res, temp_list, nums, bool_list);
                bool_list[i] = False;
                temp_list.remove(temp_list[len(temp_list) - 1]);
