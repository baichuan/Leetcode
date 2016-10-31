class Solution(object):

    def numIslands(self, grid):

        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # use DFS to solve the problem
        # search every possible directions whenever meet the new one


	# don't use visited_matrix in order to save space complexity

        row = len(grid);

        if row == 0:

            return 0;
            
        col = len(grid[0]);
        
        res = 0;
        
        for pos in range(0, row):
            
            for inpos in range(0, col):
                
                if grid[pos][inpos] == "1":
                    
                    self.DFS(pos, inpos, grid);
                    res = res + 1;
                    
        return res;
        

    def DFS(self, i, j, grid):
        
        grid[i][j] = "0";

        if i + 1 < len(grid) and grid[i + 1][j] == "1":
            
            self.DFS(i + 1, j, grid);
            
        if i - 1 >= 0 and grid[i - 1][j] == "1":
            
            self.DFS(i - 1, j, grid);
            
        if j + 1 < len(grid[0]) and grid[i][j + 1] == "1":
            
            self.DFS(i, j + 1, grid);
            
        if j - 1 >= 0 and grid[i][j - 1] == "1":
            
            self.DFS(i, j - 1, grid);


# DFS with stack --- iterative solution

class Solution(object):

    def numIslands(self, grid):

        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:

            return 0

        m,n,c,stack=len(grid), len(grid[0]),0,[]

        for a in xrange(m):

            for b in xrange(n):

                if grid[a][b]=='1':

                    stack.append((a,b))
                    c+=1

                    while stack:

                        i,j=stack.pop()
                        grid[i][j]='0'

                        if  0<=j-1<n and grid[i][j-1]=='1':

                            stack.append((i,j-1))

                        if  0<=j+1<n and grid[i][j+1]=='1':

                            stack.append((i,j+1))

                        if 0<=i+1<m and  grid[i+1][j]=='1':

                            stack.append((i+1,j))

                        if 0<=i-1<m and  grid[i-1][j]=='1':

                            stack.append((i-1,j))

        return c
