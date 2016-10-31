# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):

        """
	Encodes a tree to a single string
        :type root: TreeNode
        :rtype: str
        """

        # return as string format as "1,2,3,null,null,4,5,null,null,null,null"
        
        # use queue for BFS traverse 
        
        if root == None:
            return "";
           
        res = [];
        
        queue = [root];
        
        while queue:
            
            node = queue.pop(0);
            
            if node:

                queue.append(node.left);
                queue.append(node.right);
                res.append(str(node.val));
            
            else:
                res.append("#");
                
        return ",".join(res);
        
        
    def deserialize(self, data):

        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # This method will be invoked second, the argument data is what exactly you serialized at method "serialize", that means the data is not given by system, it's given by your own serialize method. So the format of data is designed by yourself, and deserialize it here as you serialize it in "serialize" method.
        

        if not data:
            return None;
            
        node_collection = data.split(",");
        root = TreeNode(int(node_collection[0]));
        
        i = 1;
        
        queue = [root];
        
        while queue:
            
            node = queue.pop(0);

            if node_collection[i] == "#":
                
                node.left = None;
            
            else:

                t = TreeNode(int(node_collection[i]));
                node.left = t;
                queue.append(t);
                
            i += 1;
            
            if node_collection[i] == "#":
                node.right = None;

            else:
                t = TreeNode(int(node_collection[i]));
                node.right = t;
                queue.append(t);
                
            i += 1;
            
        return root;
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
