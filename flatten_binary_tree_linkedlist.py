# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def flatten(self, root):

        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        # pre-order traversal

        if root == None:
            return None;
            
        stack = [root];
        linkedList = None;
        

        while stack:
            
            node = stack.pop();
            tleft = node.left;
            tright = node.right;
            node.left = None;
            
            if not linkedList:
                linkedList = node;
            
            else:
                linkedList.right = node;
                linkedList = linkedList.right;
                
            if tright:
                stack.append(tright);
                
            if tleft:
                stack.append(tleft);
                
        root = linkedList;
