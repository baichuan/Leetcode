import os;
import sys;

class Node:

	def __init__(self, val):

		self.val = val;
		self.left = None;
		self.right = None;


def longestConsecutive(root):
        
        if root == None:

            return 0;
            

        queue = [(root, 1)];
        max_length = 1;
        
        while queue:
            
            tuple_pair = queue.pop(0);
            node = tuple_pair[0];
            length = tuple_pair[1];
            

            if node.left:
                
                left_length = length;
                
                if node.val == node.left.val - 1:
                    left_length += 1;
                    max_length = max(max_length, left_length);
                    
                else:
                    left_length = 1;
                    
                queue.append((node.left, left_length));
                
            if node.right:
                
                right_length = length;
                
                if node.val == node.right.val - 1:
                    right_length += 1;
                    max_length = max(max_length, right_length);
                    
                else:
                    right_length = 1;
                    
	        queue.append((node.right, right_length));

            
        return max_length;


if __name__ == "__main__":

	root = Node(1)
	root.right = Node(3)
	root.right.left = Node(2)        
	root.right.right = Node(4)
	root.right.right.right = Node(5);
	res = longestConsecutive(root)

	print str(res);
