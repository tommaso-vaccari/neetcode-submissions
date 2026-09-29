class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # The core concept that I have in mind is that, to fully
        # recover an island i have to do a BFS when i find land,
        # Immagine to start from a land i can start a dfs from that land 
        # so i am able to recover all the land and insert into a set the coordinates
        # of land already explored. When i have hitted the end of the island
        # i can increment the counter for the islands and start to search fo a new isladn.

        # How to start? I can do a for loop on the grid. and consider a piece of land
        # not discovered if i have not seen it yet otherwise it has been already discovered.

        islands = 0
        seen = set()
        offsets = [[-1,0],[0,1],[1,0],[0,-1]]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    if(row,col) not in seen:
                        # I have not yet visited it so i can start a dfs visitig algorithm 
                        # from there
                        stack = list()
                        stack.append((row,col))
                        #print(stack)
                        islands +=1
                        while stack:
                            visiting = stack.pop() #Should be something like [i,j]
                            

                            # I have to add all the neighbors to the stack
                            #they are six and i add them iff they are water
                            i , j = visiting[0], visiting[1]
                            for offset in offsets:
                                n_i = i + offset[0]
                                n_j = j + offset[1]
                                if 0 <= n_i < len(grid) and 0<= n_j < len(grid[0]):
                                    if grid[n_i][n_j] == "1" :
                                        if (n_i,n_j) not in seen:
                                            stack.append((n_i,n_j))
                                            seen.add((n_i,n_j))


        return islands 
                            
                        
                    




        