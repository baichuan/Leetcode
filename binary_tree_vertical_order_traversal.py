# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def verticalOrder(self, root):

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return [];

        queue = [(root, 0)];
        
        # keep track of node with it corresponding column index
        dict = {};

        while queue:

            node, node_col_index = queue.pop(0);
            
            if node_col_index not in dict:
                
                dict[node_col_index] = [node.val];

            else:
                
                temp_list = dict[node_col_index];
                temp_list.append(node.val);
                dict[node_col_index] = temp_list;

            if node.left:
                queue.append((node.left, node_col_index - 1));

            if node.right:
                queue.append((node.right, node_col_index + 1));

        sorted_node_index_list = sorted(dict);
        res_list = [];

        for pos in range(0, len(sorted_node_index_list)):
            res_list.append(dict[sorted_node_index_list[pos]]);

        return res_list;
