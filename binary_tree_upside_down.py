import os;
import sys;

class Node:

	def __init__(self, val):

		self.val = val;
		self.left = None;
		self.right = None;

def upsideDownBinaryTree(root):

        stack = [];
        
        head = Node(0);
        cur = head;
        
        while root:

            stack.append(root);
            root = root.left;
            
        while stack:

            node = stack.pop();
            cur.right = node;
            
            if stack:
                node.left = stack[-1].right;
                
            cur = cur.right;
            
        return head.right;



if __name__ == "__main__":

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)        
	root.left.right = Node(5)
	
	res = upsideDownBinaryTree(root);

	print str(res.val);
