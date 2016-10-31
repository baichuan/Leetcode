class Solution(object):

    # time complexity O(2^{n})
    # space: O(n)

    def helper(self, digits, dict, resList, tempStr, currIndex):
        
        if len(tempStr) == len(digits):

            resList.append(tempStr);
            return;

        currDigits = digits[currIndex];
        phoneList = dict[currDigits];

        for i in range(0, len(phoneList)):

            tempStr = tempStr + str(phoneList[i]);
            self.helper(digits, dict, resList, tempStr, currIndex + 1);
            tempStr = list(tempStr);
            del tempStr[-1];
            tempStr = "".join(tempStr);

    def letterCombinations(self, digits):

        """
        :type digits: str
        :rtype: List[str]
        """

        dict = {'0':[], '1':[], '2':['a','b','c'], '3':['d','e', 'f'], '4':['g','h','i'], '5':['j', 'k', 'l'], '6':['m','n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']};

        resList = [];
        tempStr = "";

        if digits == "":
            return [];

        # keep track of the current index of digits
        currIndex = 0;
        self.helper(digits, dict, resList, tempStr, currIndex);

        return resList;
