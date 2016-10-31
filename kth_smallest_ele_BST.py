# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    
        def walk_in_order(self, x, res_list):

            if x != None:
            
                self.walk_in_order(x.left, res_list);
                res_list.append(x.val);
                self.walk_in_order(x.right, res_list);

   
        def kthSmallest(self, root, k):

            """
            :type root: TreeNode
            :type k: int
            :rtype: int
            """

            res_list = [];
            self.walk_in_order(root, res_list);
            return res_list[k-1];
