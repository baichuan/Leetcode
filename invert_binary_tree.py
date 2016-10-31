# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def invertTree(self, root):

        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # BFS solution
        if root == None:

            return None;

        level = [root];

        while level:

            ls = [];

            for node in level:

                if node.left:

                    ls.append(node.left);

                if node.right:

                    ls.append(node.right);
                    
                node.left, node.right = node.right, node.left;

            level = ls;

        return root;   
