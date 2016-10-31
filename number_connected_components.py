class Solution(object):

    def countComponents(self, n, edges):

        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        # build the adjacent list for each node in the graph

        neighbors = {i:[] for i in range(0, n)};
        
        for v, w in edges:

            neighbors[v].append(w);
            neighbors[w].append(v);


        # For BFS, build the visited node bool List
        visited_list = [False] * n;

        res = 0;

        for i in range(0, n):

            if visited_list[i] == False:
                
                res += 1;
                queue = [i];
                visited_list[i] = True;

                while queue:

                    curr_node = queue.pop(0);

                    for k in neighbors[curr_node]:

                        if visited_list[k] == False:
                            visited_list[k] = True;
                            queue.append(k);

        return res;
