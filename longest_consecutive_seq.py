class Solution(object):

    def longestConsecutive(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        

        # create an hash set and put all elements into the hash set
        # for each element, check if this element is the starting point of the sequence. In order to check this, we look for nums[i] - 1 in hash. If not found, then this is the first element in the sequence.
        
        # if this element is the first element in the sequence, then count the number of elements in the consecutive starting with this element.
        
        # example: [1, 16, 4, 17, 3, 2, 2, 17]
        
        # time complexity: O(n)
        
        hash_set = set();
        
        maxLength = 0;
        
        for i in range(0, len(nums)):
            hash_set.add(nums[i]);
            
        for i in range(0, len(nums)):
            
            # if the current element is the starting element of a consecutive sequence
            if nums[i] - 1 not in hash_set:
                
                # check the next element in the sequence
                j = nums[i];

                while j in hash_set:
                    j += 1;
                
                # update optimal length 
                
                if maxLength < j - nums[i]:
                    maxLength = j - nums[i];
                    
        return maxLength;
