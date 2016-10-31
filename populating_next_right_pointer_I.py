# Definition for binary tree with next pointer.

# class TreeLinkNode:

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:

    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        
        if root == None:
            
            return root;
            
        queue = [];
        keep_height = 1;
        queue.append((root, 1));
        
        pre_node = root;
        
        while queue:
            
            node, height = queue.pop(0);
                
            if keep_height == height:
                pre_node.next = node;        
            
            elif height == keep_height + 1:
                pre_node.next = None;
                
            keep_height = height;
            pre_node = node;
            
            if node.left:
                queue.append((node.left, height + 1));
                
            if node.right:
                queue.append((node.right, height + 1));
                
        pre_node.next = None;
