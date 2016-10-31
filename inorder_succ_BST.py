# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    
    def findParent(self, root, p):    

        stack = [root];
        kid_parent_dict = {root: None};

        while p not in kid_parent_dict:
            
            node = stack.pop();
            
            if node.left:
                kid_parent_dict[node.left] = node;
                stack.append(node.left);

            if node.right:
                kid_parent_dict[node.right] = node;
                stack.append(node.right);

        return kid_parent_dict;
        

    def treeMin(self, x):

        while x.left != None:
            x = x.left;

        return x;
        
    def inorderSuccessor(self, root, p):

        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        # whether p has right child
        
        if p.right != None:

            return self.treeMin(p.right);

        kid_parent_dict = self.findParent(root, p);
        y = kid_parent_dict[p];

        while y != None and p == y.right:
            
            p = y;
            y = kid_parent_dict[y];

        return y;
