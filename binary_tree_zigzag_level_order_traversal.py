# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return [];

        res_list = [];
        curr_level = [root];
        level_count = 0;

        while curr_level:

            next_level = [];
            temp_list = [];

            # at odd level of tree
            if level_count % 2 == 1:

                for i in range(0,len(curr_level)):
                    temp_list.append(curr_level[i].val)

                    # if current level has child, then append the value into next level list
                    if curr_level[len(curr_level)-i-1].left: 
                        next_level.append(curr_level[len(curr_level)-i-1].left);

                    if curr_level[len(curr_level)-i-1].right: 
                        next_level.append(curr_level[len(curr_level)-i-1].right);

                curr_level = next_level
                res_list.append(temp_list);

            # at even level of tree
            elif level_count % 2 == 0:
            
	  	for i in range(0, len(curr_level)):
                    temp_list.append(curr_level[i].val);

                    if curr_level[len(curr_level) - i - 1].right: 
                        next_level.append(curr_level[len(curr_level)-i-1].right);

                    if curr_level[len(curr_level)-i-1].left:
                        next_level.append(curr_level[len(curr_level)-i-1].left);

                curr_level = next_level;
                res_list.append(temp_list);

            level_count = level_count + 1;
            
        return res_list;
