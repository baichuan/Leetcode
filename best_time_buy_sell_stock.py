class Solution(object):

    def maxProfit(self, prices):

        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 1:
            return 0;

        if len(prices) == 0:
            return 0;

        # build a profit list
        profit_list = [];

        for i in range(1, len(prices)):
            profit_list.append(prices[i] - prices[i-1]);

        prefix_sum = profit_list[0];
        max_sum = profit_list[0];

        for i in range(1, len(profit_list)):

            if profit_list[i] > prefix_sum + profit_list[i]:
                prefix_sum = profit_list[i];

            else:
                prefix_sum = prefix_sum + profit_list[i];

            if max_sum < prefix_sum:
                max_sum = prefix_sum;

        if max_sum > 0:
            return max_sum;

        else:
            return 0;


class Solution(object):

    def maxProfit(self, prices):

        """
        :type prices: List[int]
        :rtype: int
        """

        min_index = 0;
        max_diff = 0;
        sell_index = 0;
        buy_index = 0;

        for i in range(0,len(prices)):

            if prices[i] < prices[min_index]:
                min_index = i;

            diff = int(prices[i] - prices[min_index]);

            if diff > max_diff:

                buy_index = min_index;
                sell_index = i;
                max_diff = diff;

        return max_diff;
