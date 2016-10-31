# followup 哪些地方应该handle exception。答了number和operator数对不上，还有number不valid，operator不valid的情况。之后按照要求写了try throw和catch

class Solution(object):

    def evalRPN(self, tokens):

        """
        :type tokens: List[str]
        :rtype: int
        """
        
        # use a stack.
        # look through each element in the given array. When it is a number, push it to the stack. when it is a operator, pop two numbers from the stack and do the calculation, and push back the result to the stack

        
        operators = "+-*/";
        stack = [];

        for i in range(0, len(tokens)):
            
            if tokens[i] not in operators:

                # token is a number
                stack.append(tokens[i]);
                
            else:

                a = int(stack.pop());
                b = int(stack.pop());
                
                if tokens[i] == "+":
                    stack.append(str(a + b));

                elif tokens[i] == "-":
                    stack.append(str(b - a));

                elif tokens[i] == "*":
                    stack.append(str( a * b));

                # in Python, -1 / 2 = -1; 
                # in java, -1 / 2 = 0, which is by default of Leetcode

                elif tokens[i] == "/":
                    if a * b < 0:
                        stack.append(-((-b) / a));
                        
                    else:
                        stack.append(str(b / a));

        return int(stack.pop());
