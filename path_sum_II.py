# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def pathSum(self, root, s):

        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        # stack + DFS

        if root == None:

            return [];

        res = [];
        stack = [(root, [root.val])];

        while stack:
            
            tuple_pair = stack.pop();
            node = tuple_pair[0];
            ls = tuple_pair[1];

            if not node.left and not node.right and sum(ls) == s:
                res.append(ls);

            elif node.left and not node.right:
                stack.append((node.left, ls + [node.left.val]));

            elif node.right and not node.left:
                stack.append((node.right, ls + [node.right.val]));

            elif node.left and node.right:
                stack.append((node.left, ls + [node.left.val]));
                stack.append((node.right, ls + [node.right.val]));

        return res;
