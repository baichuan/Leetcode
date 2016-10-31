class Solution(object):

    def increasingTriplet(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # find the smallest element in 3 subsequence
        # find the second one greater than the first one. If not, reset the first one
        

        fst = sys.maxint;
        snd = sys.maxint;
        
        for i in range(0, len(nums)):
            
            if nums[i] <= fst:
                fst = nums[i];
                
            elif nums[i] <= snd:
                snd = nums[i];
            
            else:
                return True;
                
        return False;
