# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):

        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        while root:
            
            if root.val > p.val and root.val > q.val:

                # left subtree
                root = root.left;

            elif root.val < p.val and root.val < q.val:

                # right subtree
                root = root.right;

            else:
        
                return root;


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):

        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # recursion version

        if (root.val - p.val) * (root.val - q.val) <= 0:
            return root;

        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q);

        else:
            return self.lowestCommonAncestor(root.right, p, q);
