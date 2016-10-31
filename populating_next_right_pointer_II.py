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
        
        # BFS + queue
        
        if root == None:
            return root;
            
        queue = [];
        height = 1;
        keep_height = 1;
        queue.append((root, 1));
        pre_node = root;
        
        while queue:
            
            node, height = queue.pop(0);

            # current node and previous node in the different level

            if height == keep_height + 1:
                pre_node.next = None;
            
            # current node and previous node in same level
            elif height == keep_height:
                pre_node.next = node;
                
            keep_height = height;
            pre_node = node;
            
            if node.left:
                queue.append((node.left, height + 1));
                
            if node.right:
                queue.append((node.right, height + 1));
                
        # last node in the tree points to null as well
        pre_node.next = None;
