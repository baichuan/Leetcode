class Solution(object):

    def combinationSum(self, candidates, target):

        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = [];
        
        if candidates == []:

            return [];
        

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
                
                temp_list.append(candidates[i]);
                self.helper(res, temp_list, candidates, target - candidates[i], i); # not i + 1 because we can reuse same element
                temp_list.remove(temp_list[len(temp_list) - 1]);
