class Solution(object):

    def wallsAndGates(self, rooms):

        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        if rooms != []:
        
            inf = 2**31 - 1;
        
            row = len(rooms);
            col = len(rooms[0]);

            # put all the positions with 0 value into queue as initialization step in BFS (layer 0)
        
            queue = [];

            for i in range(0, row):

                for j in range(0, col):                

                    if rooms[i][j] == 0:
                        queue.append((i, j));

            # here we don't need visited_cell set, as the value of each cell itself can be the visted evidence. If the value is inf, then not visited. Otherwise it is visited

            while queue:
            
                r, c = queue.pop(0);
            
                if r + 1 < row and rooms[r + 1][c] == inf:

                    rooms[r + 1][c] = rooms[r][c] + 1;
                    queue.append((r + 1, c));

                    
                if r - 1 >= 0 and rooms[r - 1][c] == inf:

                    rooms[r - 1][c] = rooms[r][c] + 1;
                    queue.append((r - 1, c));

                
                if c + 1 < col and rooms[r][c + 1] == inf:

                    rooms[r][c + 1] = rooms[r][c] + 1;
                    queue.append((r, c + 1));

                
                if c - 1 >= 0 and rooms[r][c - 1] == inf:

                    rooms[r][c - 1] = rooms[r][c] + 1;
                    queue.append((r, c - 1));
