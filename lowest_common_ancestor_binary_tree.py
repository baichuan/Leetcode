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

	# have to ask interviewer whether ancestor should be itself

        stack = [root];
        kid_parent_dict = {root: None};

        while p not in kid_parent_dict or q not in kid_parent_dict:            

            node = stack.pop();

            if node.left:
                kid_parent_dict[node.left] = node;
                stack.append(node.left);

            if node.right:
                kid_parent_dict[node.right] = node;
                stack.append(node.right);

        ancestor_set = set();
        
        while p:

            ancestor_set.add(p);
            p = kid_parent_dict[p];
            
        while q not in ancestor_set:
            
            q = kid_parent_dict[q];

        return q;
