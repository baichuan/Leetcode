# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):

    def Helper(self, root):

        if root == None:
            return (0, 0);

        leftTuple = self.Helper(root.left);
        rightTuple = self.Helper(root.right);
        return (root.val + leftTuple[1] + rightTuple[1], max(leftTuple) + max(rightTuple));

        
    def rob(self, root):

        """
        :type root: TreeNode
        :rtype: int
        """
        resTuple = self.Helper(root);
        return max(resTuple);
