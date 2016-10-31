class Solution(object):

    def numberToWords(self, num):

        """
        :type num: int
        :rtype: str
        """

        dict = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"};
        
        res_list = [];
        
        if num == 0:
            return dict[0];
            
        if num >= 1000000000:

            remain = num / 1000000000;
            res_list.append(self.transformer(remain) + " Billion");
            num = num % 1000000000;
            

        if num >= 1000000:

            remain = num / 1000000;
            res_list.append(self.transformer(remain) + " Million");
            num = num % 1000000;
            
        if num >= 1000:

            remain = num / 1000;
            res_list.append(self.transformer(remain) + " Thousand");
            num = num % 1000;
            

        if num > 0:
            res_list.append(self.transformer(num));
            
        return "".join(res_list).strip();
        
    
    def transformer(self, num):
        
        dict = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"};
        
        temp_list = [];
        
        if num >= 100:

            div_res = num / 100;
            temp_list.append(" " + str(dict[div_res]) + " Hundred");
            num = num % 100;

        if num > 0:
            
            if num > 0 and num <= 20:
                temp_list.append(" " + str(dict[num]));
                
            else:
                div_res = num / 10;
                temp_list.append(" " + str(dict[div_res * 10]));
                num = num % 10;
                
                if num > 0:
                    temp_list.append(" " + str(dict[num]));
        
        return "".join(temp_list);
