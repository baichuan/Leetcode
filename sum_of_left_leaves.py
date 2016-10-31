import os;
import sys;


class Node:

	def __init__(self, val):

		self.val = val;
		self.left = None;
		self.right = None;


def sumOfLeftLeaves(root):

	if root == None:
    		return 0;

	res = 0;
        queue = [root];

        while queue:

            node = queue.pop(0);

	    # left leaves

            if node.left and node.left.left == None and node.left.right == None:
                res += node.left.val;
                
            if node.left:
                queue.append(node.left);
                
            if node.right:
                queue.append(node.right);
                
                
        return res;


if __name__ == "__main__":

	root = Node(3)
	root.left = Node(9)
	root.right = Node(20)
	root.right.left = Node(15)        
	root.right.right = Node(7)
	res = sumOfLeftLeaves(root)

	print str(res);
