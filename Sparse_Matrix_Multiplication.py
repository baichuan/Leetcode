class Solution(object):

    def multiply(self, A, B):

        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        A_sparse = [];
    	for pos in range(0, len(A)):
    		colATupleList = [];
    		for inpos in range(0, len(A[pos])):
    			if A[pos][inpos] != 0:
    				colATupleList.append((inpos, A[pos][inpos]));
    		A_sparse.append(colATupleList);

    	B_sparse = [];
    	row_B = len(B);
    	col_B = len(B[0]);
    	colB_index = 0;

    	while colB_index < col_B:

    		rowB_index = 0;
    		rowBTupleList = [];
    		while rowB_index < row_B:
    			if B[rowB_index][colB_index] != 0:
    				rowBTupleList.append((rowB_index, B[rowB_index][colB_index]));
    			rowB_index = rowB_index + 1;
    		B_sparse.append(rowBTupleList);
    		colB_index = colB_index + 1;


    	# do A*B multiplication
    	C = [];
    	for i in range(0, len(A_sparse)):
    		C_row = [];	
    		for j in range(0, len(B_sparse)):
    			cellSum = 0;
    			A_row = A_sparse[i];
    			B_col = B_sparse[j];
    			a_index = 0;
    			b_index = 0;
    			while a_index < len(A_row) and b_index < len(B_col):
    				if A_row[a_index][0] == B_col[b_index][0]:
    					cellSum = cellSum + A_row[a_index][1] * B_col[b_index][1];
    					a_index = a_index + 1;
    					b_index = b_index + 1;

    				elif A_row[a_index][0] < B_col[b_index][0]:
    					a_index = a_index + 1;

    				else:
    					b_index = b_index + 1;

    			C_row.append(cellSum);
    		C.append(C_row);

    	return C;		
