# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def CheckBST(self, root, min, max):

        if root == None:
            return True;

        if root.val <= min or root.val >= max:
            return False;

        return self.CheckBST(root.left, min, root.val) and self.CheckBST(root.right, root.val, max);

        
    def isValidBST(self, root):

        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.CheckBST(root, -2147483649, 2147483648);


# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isValidBST(self, root):

        """
        :type root: TreeNode
        :rtype: bool
        """

        stack = [];
        res = [];
        
        while stack or root:
            
            if root:
                stack.append(root);
                root = root.left;
                
            else:
                
                node = stack.pop();
                
                if res and node.val <= res[-1]:
                    return False;
                    
                res.append(node.val);
                root = node.right;
        
        return True;
