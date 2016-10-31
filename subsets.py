# give an example for backtracking [1,2,3]

class Solution(object):

    
    def helper(self, resListList, subList, startIndex, nums):
        
        for i in range(startIndex,len(nums)):

            subList.append(nums[i]);
            subListCopy = list(subList);
            resListList.append(subListCopy);
            self.helper(resListList, subList, i + 1, nums);
            subList.remove(subList[len(subList) - 1]);
            


    def subsets(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        resListList = [];
        subList = [];
        resListList.append(subList);
        
        if nums == []:
            return [[]];
            
        startIndex = 0;
        self.helper(resListList, subList, startIndex, nums);
        
        return resListList;
