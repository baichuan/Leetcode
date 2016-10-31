def validTree(n, edges):

        # for a connected graph with n nodes, the min number of edges to make graph connected is (n - 1), which is a tree structure
        
        nodeList = range(0, n);

        if len(edges) != n - 1:

            return False;

        # left is to check whether there is isolated components in graph --- BFS

        adj_dict = {};
        
        for i in range(0, len(edges)):
            
            source_node = edges[i][0];
            dest_node = edges[i][1];

            if source_node not in adj_dict:
                adjList = [dest_node];
                adj_dict[source_node] = adjList;

            else:
                
                adjList = adj_dict[source_node];
                adjList.append(dest_node);
                adj_dict[source_node] = adjList;

            if dest_node not in adj_dict:
                adjList_ = [source_node];
                adj_dict[dest_node] = adjList_;

            else:
                
                adjList_ = adj_dict[dest_node];
                adjList_.append(source_node);
                adj_dict[dest_node] = adjList_;

        for pos in range(0, len(nodeList)):
            if nodeList[pos] not in adj_dict:
                adj_dict[nodeList[pos]] = [];

        queue = [0];
        
        while queue:
            
            node = queue.pop(0);

            if node in adj_dict:
                queue = queue + adj_dict[node];
                adj_dict.pop(node);

                
        return not adj_dict;


# compact version of code

def validTree(self, n, edges):

	if len(edges) != n - 1:
		return False;

	neighbors = {i:[] for i in range(n)};
	
	for v, w in edges:
		neighbors[v].append(w);
		neighbors[w].append(v);

	queue = [0];
	
	while queue:

		queue.extend(neighbors.pop(queue.pop(0), []));

	return not neighbors
