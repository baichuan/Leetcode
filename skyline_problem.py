class Solution(object):

    # https://segmentfault.com/a/1190000003786782

    def getSkyline(self, buildings):

        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

	# currently the code is not accepted in LC as some corner case cannot handle
	# test case: [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]

        # 如果按照一个矩形一个矩形来处理将会非常麻烦，我们可以把这些矩形拆成两个点，一个左上顶点，一个右上顶点。将所有顶点按照横坐标排序后，我们开始遍历这些点。遍历时，通过一个堆来得知当前图形的最高位置。堆顶是所有顶点中最高的点，只要这个点没被移出堆，说明这个最高的矩形还没结束。对于左顶点，我们将其加入堆中。对于右顶点，我们找出堆中其相应的左顶点，然后移出这个左顶点，同时也意味这这个矩形的结束。具体代码中，为了在排序后的顶点列表中区分左右顶点，左顶点的值是正数，而右顶点值则存的是负数

        res = [];

        # store 每个矩形左右上顶点
    
        height = [];
        
        for b in buildings:
            
            # 左上顶点存为负数
            height.append([b[0], -b[2]]);
            
            # 右上顶存为正数
            height.append([b[1], b[2]]);
            
        # sort the height based on x-coordinate
        height.sort(key=lambda x: x[0]);
        
        # build an array
        arr = [];
        arr.append(0);
        
        # prev to record previous keypoint's height
        prev = 0;
        
        for h in height:
            # push the left corner into the array
            if h[1] < 0:
                arr.append(-h[1]);
            
            else:
                # 将右上顶点对应的左上顶点移除
                arr.remove(h[1]);
            
            cur = max(arr);
            
            # 如果arr的max和上个keypoint高度不一样，则加入一个新的keypoint
            
            if prev != cur:
                res.append([h[0], cur]);
                prev = cur;
                
        return res;
