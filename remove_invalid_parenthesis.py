class Solution(object):

    def removeInvalidParentheses(self, s):

        """
        :type s: str
        :rtype: List[str]
        """
        
        # BFS + queue
        # remove one symbol --- layer 1
        # remove two symbols --- layer 2
        # ....
        
        if not s:
            return [""];
            
        queue = [s];
        res = [];
        visited = set();
        
        found = False;
        
        while queue:
            
            cur = queue.pop(0);
            
            # if found, then return as we need to remove the minimum number of invalid parentheses to make the input string valid
            # 因为要去除最少括号，所以即使有其他的结果，也一定在同一层
           
            if self.isValidParenthesis(cur):

                found = True;
                res.append(cur);

            elif not found:
                
                for i in range(0, len(cur)):
                    
                    if cur[i] == "(" or cur[i] == ")":
                        
                        t = cur[0:i] + cur[i+1:];
                        
                        if t not in visited:
                            queue.append(t);
                            visited.add(t);
            
        return res;
        
        
    def isValidParenthesis(self, string):
            
        count = 0;
            
        for c in string:
                
            if c == "(":
                count += 1;
                    
            elif c == ")":
                if count == 0:
                    return False;

                count -= 1;
            
        return count == 0;
