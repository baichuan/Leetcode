# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):

        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root == None:
            return False;

        if root.left == None and root.right == None:
            return root.val == sum;

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val);


# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):

        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root == None:
            return False;

        stack = [];
        stack = [(root, 0)];

        while stack:

            tuple_pair = stack.pop();
            node = tuple_pair[0];
            path_sum = tuple_pair[1];

            if node.left and node.right:

                stack.append((node.left, path_sum + node.val));
                stack.append((node.right, path_sum + node.val));

            elif node.left and not node.right:

                stack.append((node.left, path_sum + node.val));

                
            elif node.right and not node.left:

                stack.append((node.right, path_sum + node.val));

            else:

                if path_sum + node.val == sum:
                    return True;

        return False;
