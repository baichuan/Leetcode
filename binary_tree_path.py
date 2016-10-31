# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    # @param {TreeNode} root
    # @return {string[]}

    def binaryTreePaths(self, root):

        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res


    def dfs(self, node, path, res):

        if not node:
            return

        if not node.left and not node.right:
            res.append("{}{}".format(path, node.val))
        self.dfs(node.left, "{}{}->".format(path, node.val), res)
        self.dfs(node.right, "{}{}->".format(path, node.val), res)



# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # @param {TreeNode} root
    # @return {string[]}

    def binaryTreePaths(self, root):
        
        # DFS with stack
        
        if root == None:
            
            return [];
            
        res = [];
        stack = [(root, str(root.val))];
        
        while stack:
            
            tuple_pair = stack.pop();
            node = tuple_pair[0];
            path_str = tuple_pair[1];
            
            if node.left:
                
                stack.append((node.left, path_str + "->" + str(node.left.val)));
                
            if node.right:
                
                stack.append((node.right, path_str + "->" + str(node.right.val)));
                
            if not node.left and not node.right:
                
                res.append(path_str);
                
        return res;


# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, x):

#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    # @param {TreeNode} root
    # @return {string[]}

    def binaryTreePaths(self, root):

        # BFS solution with queue

        if root == None:

            return [];
            
        res = [];
        queue = [(root, str(root.val))];

        while queue:

            tuple_pair = queue.pop(0);
            node = tuple_pair[0];
            path_str = tuple_pair[1];

            if not node.left and not node.right:

                res.append(path_str);
                continue;

            if node.left:
                
                queue.append((node.left, path_str + "->" + str(node.left.val)));

            if node.right:

                queue.append((node.right, path_str + "->" + str(node.right.val)));
                
        return res;
