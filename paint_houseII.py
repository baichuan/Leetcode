class Solution(object):

    def minCostII(self, costs):

        """
        :type costs: List[List[int]]
        :rtype: int
        """

        if len(costs) == 0:
            return 0;

        for i in range(1, len(costs)):
            for j in range(0, len(costs[0])):
                min_cost = sys.maxint;
                for z in range(0, len(costs[0])):
                    if z != j:
                        if costs[i][j] + costs[i-1][z] < min_cost:
                            min_cost = costs[i][j] + costs[i-1][z];
                        
                costs[i][j] = min_cost;
                
        res_min = sys.maxint;
        for pos in range(0, len(costs[0])):
            if costs[len(costs)-1][pos] < res_min:
                res_min = costs[len(costs)-1][pos];

        return res_min;
