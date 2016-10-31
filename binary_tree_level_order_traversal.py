# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return [];

        res_list = [];
        curr_level = [root];

        while curr_level:

            next_level = [];
            temp_list = [];

            for i in range(0, len(curr_level)):

                temp_list.append(curr_level[i].val);

                if curr_level[i].left:
                    next_level.append(curr_level[i].left);

                if curr_level[i].right:
                    next_level.append(curr_level[i].right);

            curr_level = next_level;
            res_list.append(temp_list);

        return res_list;


# BFS

# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # BFS
        
        if not root:
            
            return [];
            
        queue = [root];
        res = [];
        
        while queue:
            
            level_list = [];
            size = len(queue);

            for i in range(0, size):
                
                node = queue.pop(0);
                level_list.append(node.val);
                
                if node.left:
                    queue.append(node.left);
                    
                if node.right:
                    queue.append(node.right);
                    
            res.append(level_list);
            
        return res;
