# Definition for a undirected graph node

# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution(object):

    def cloneGraph(self, node):

        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """

        if node == None:
            return None;

        copyNode = UndirectedGraphNode(node.label);

        dict = {};
        
        dict[node] = copyNode;
	queue = [node];
	
	while queue:

            curr = queue.pop(0);

            for n in curr.neighbors:
                
                if n in dict:
                    
                    dict[curr].neighbors.append(dict[n]);
                    
                else:
                    
                    nCopy = UndirectedGraphNode(n.label);
                    dict[n] = nCopy;
                    dict[curr].neighbors.append(nCopy);

                    queue.append(n);
                    
        return dict[node];
