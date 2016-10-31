class Solution(object):

    def combinationSum2(self, candidates, target):

        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort();
        
        if candidates == []:

            return [];
            
        res = [];
        temp_list = [];
        
        start_index = 0;
        
        self.helper(res, temp_list, candidates, target, start_index);
        
        return res;
        
    
    def helper(self, res, temp_list, candidates, target, start_index):
        
        if target < 0:
            return;
            
        elif target == 0:
            
            copy_list = list(temp_list);
            res.append(copy_list);
            return;
            
        else:

            for i in range(start_index, len(candidates)):
                
                if i > start_index and candidates[i] == candidates[i - 1]: # skip duplicates
                    continue;
                    
                else:
                    
                    temp_list.append(candidates[i]);
                    self.helper(res, temp_list, candidates, target - candidates[i], i + 1);
                    temp_list.remove(temp_list[len(temp_list) - 1]);
