# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findLeaves(self, root):

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = [];

        if root == None:

            return res;

        stack = [];

        while root.left != None or root.right != None:
            
            stack.append(root);
            temp = [];

            while stack:

                node = stack.pop();

                if node.left != None:

                    if node.left.left == None and node.left.right == None:
                        temp.append(node.left.val);
                        node.left = None;

                    else:
                        stack.append(node.left);

                if node.right != None:

                    if node.right.left == None and node.right.right == None:
                        temp.append(node.right.val);
                        node.right = None;

                    else:
                        stack.append(node.right);

            res.append(temp);

        res.append([root.val]);

        return res;
