# Assume each array has exactly one solution

class Solution(object):
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

	# time complexity O(n)

        index_dict = {};

        for i in range(0, len(nums)):
            key = target - nums[i];
            if key in index_dict:
                return [index_dict[key], i];
            else:
                index_dict[nums[i]] = i;
        return [];



class Solution(object):

    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # time complexity O(n*lgn)
        # sorting         

        sorted_nums = sorted(nums);

        index1 = -1;
        index2 = -1;
        
        start = 0;
        end = len(sorted_nums) - 1;

        while start < end:
            
            if sorted_nums[start] + sorted_nums[end] == target:

                # not the case for 0 + 0 = target = 0

                if sorted_nums[start] != sorted_nums[end]:

                    for i in range(0, len(nums)):
                
                        if nums[i] == sorted_nums[start]:

                            index1 = i;
                            break;                        

                    for j in range(0, len(nums)):

                        if nums[j] == sorted_nums[end]:
                        
                            index2 = j;
                            break;
                    
                else:

                    # case of 0 + 0 = target = 0

                    for i in range(0, len(nums)):

                           if nums[i] == sorted_nums[start]:                 
                           	index1 = i;
			   	break;
			
		    for j in range(0, len(nums)):

                    	if nums[j] == sorted_nums[end] and j != index1:

                        	index2 = j;
                            	break;

                return [index1, index2];
                
            elif sorted_nums[start] + sorted_nums[end] < target:

                start += 1;
                
            else:

                end -= 1;
                
        return [];
