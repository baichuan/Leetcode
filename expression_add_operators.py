class Solution(object):  

    # 有可能string很长，所以要用长整数
    # 需要记录last oprand，为的是处理乘号的情况。乘号时的计算公式为: result - lastOP + lastOP * curVaule，如 2 + 3 * 5, 当计算到要乘5时，result = 2 + 3 = 5, lastOp = 3, curValue = 5, 则最终结果为： 5 - 3 + 3 * 5 = 17 = 2 + 3 * 5
    # 记录当前结果，用于在num长度为零时， 判断是否与target相等，并加入最终的results中
    # 需要跳过长于一个零的操作数，如“00”， “000”， etc.
    # 按左操作数从长度为1 到长度为len(num)循环， 并递归

    def addOperators(self, num, target):  

        """ 
        :type num: str 
        :type target: int 
        :rtype: List[str] 
        """  

        results = []  
        self.opRecur(num, target, 0, 0, "", results)  

        return results  
          
    def opRecur(self, num, target, lastOp, result, expression, results):  

        if len(num) == 0:  
            if target == result:  
                results.append(expression)  
            return  
          
        for i in range(1, len(num) + 1):  

            cur = num[:i]  
            if len(cur) > 1 and cur[0] == "0":  
                continue  

            rest = num[i:]  
            curV = int(cur)  

            if len(expression) == 0:  
                self.opRecur(rest, target, curV, curV, expression + cur, results)  

            else:  
                self.opRecur(rest, target, curV, result + curV, expression + "+" + cur, results)  
                self.opRecur(rest, target, -curV, result - curV, expression + "-" + cur, results)  
                self.opRecur(rest, target, lastOp * curV, result - lastOp + lastOp * curV, expression + "*" + cur, results) 
