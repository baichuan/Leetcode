import os;
import sys;

def getFactors(n):


	# keep track of 12
	# [2, 6], [2, 2, 3], [3, 4]

	res = [];
	temp_list = [];
	helper(2, 1, n, res, temp_list);

	return res;


def helper(start, product, n, res, temp_list):

	if start > n or product > n:
    		return;
    
	if product == n:
    
    		copy_list = list(temp_list);
    		res.append(copy_list);
    		return;
    
	for i in range(start, n):
    
    		if i * product > n:
			break;
	
    		if n % i == 0:

			temp_list.append(i);
			helper(i, i*product, n, res, temp_list);
			temp_list.remove(temp_list[len(temp_list) - 1]);



if __name__ == "__main__":

	n = 12;

	res = getFactors(n);
	print str(res)
