# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# iterative: time complexity O(number of nodes); space complexity: O(max number of nodes in one level)
# recursive: time complexity O(number of nodes); space complexity: O(lgn) if tree balance. Otherwise space complexity is O(n)

class Solution(object):

    def maxDepth(self, root):

        """
        :type root: TreeNode
        :rtype: int
        """

        # no recursion and level order traversal

        if root == None:
            return 0;

        node_list = [];
        node_list.append((root, 1));
        max_height = 1;

        while node_list:

            node, height = node_list.pop(0);

            if height > max_height:
                max_height = height;

            if node.left:
                node_list.append((node.left, height + 1));

            if node.right:
                node_list.append((node.right, height + 1));

        return max_height;



# Definition for a binary tree node.
# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def maxDepth(self, root):

        """
        :type root: TreeNode
        :rtype: int
        """

	# recursion

        if root == None:
            return 0;

        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1;
