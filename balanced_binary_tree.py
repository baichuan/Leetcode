# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    
    def getheight(self, root):
    
        if root == None:
            return 0;

        return max(self.getheight(root.left), self.getheight(root.right)) + 1;

    def isBalanced(self, root):

        """
        :type root: TreeNode
        :rtype: bool
        """

        if root == None:
            return True;

        if abs(self.getheight(root.left) - self.getheight(root.right)) > 1:
            return False;

        return self.isBalanced(root.left) and self.isBalanced(root.right);
