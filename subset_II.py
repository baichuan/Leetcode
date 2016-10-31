class Solution(object):

    def subsetsWithDup(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort();
        resListList = [];
        subList = [];

        # include empty set into the result
        resListList.append(subList);
        
        if nums == []:
            return [[]];
            
        startIndex = 0;
        self.dfs(resListList, subList, startIndex, nums);
        
        return resListList;
        
    
    def dfs(self, resListList, subList, startIndex, nums):
        
        for i in range(startIndex, len(nums)):
            
            # skip duplicate element
            if i > startIndex and nums[i] == nums[i - 1]:
                continue;
                
            else:
                
                subList.append(nums[i]);
                subListCopy = list(subList);
                resListList.append(subListCopy);
                
                self.dfs(resListList, subList, i + 1, nums);
                subList.remove(subList[len(subList) - 1]);
