# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def Check(self, p, q):

        if p == None and q == None:
            return True;

        if p and q:

            if p.val == q.val:
                return self.Check(p.right, q.left) and self.Check(p.left, q.right);

        return False;


    def isSymmetric(self, root):

        """
        :type root: TreeNode
        :rtype: bool
        """

        if root:

            return self.Check(root.left, root.right);

        return True;
