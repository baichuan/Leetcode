# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sumNumbers(self, root):

        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0;

        res_sum = 0;
        stack = [(root, str(root.val))];

        while stack:
            
            tuple_pair = stack.pop();
            node = tuple_pair[0];
            path_str = tuple_pair[1];

            if node.left and node.right:

                stack.append((node.left, path_str + str(node.left.val)));
                stack.append((node.right, path_str + str(node.right.val)));

            elif node.right and not node.left:

                stack.append((node.right, path_str + str(node.right.val)));

            elif node.left and not node.right:

                stack.append((node.left, path_str + str(node.left.val)));

            else:
                
                res_sum = res_sum + int(path_str);

        return res_sum;
