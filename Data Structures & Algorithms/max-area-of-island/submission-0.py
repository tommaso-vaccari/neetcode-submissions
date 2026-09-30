class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #UMPIRE: Understand Match Plan Implement Review Evaluate
        # I have an island on which the land is 1ones and i have to search for the biggest
        # one pretty similar to ones that I have already seen. 
        # The idea is visiting using DFS algorithm and to keep count when i start from 
        # fresh land of the area and keep only the max area.


        seen = set() #Coordinate (i,j)
        stack = list() #Coordinates [i,j] pop and append for the dfs algorithm
        offsets = [[-1,0],[0,1],[1,0],[0,-1]]
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row,col) not in seen:
                    # I have a starting point for the dfs algorithm
                    stack.append([row,col])
                    visited = set()
                    visited.add((row,col))
                    seen.add((row,col))
                    area = 0
                    while stack:
                        i, j = stack.pop()
                        area+=1
                        for offset in offsets:
                            n_i = i + offset[0]
                            n_j = j + offset[1]
                            if 0<=n_i<len(grid) and 0<=n_j <len(grid[0]):
                                if grid[n_i][n_j] == 1:
                                    if (n_i,n_j) not in visited:
                                        stack.append([n_i,n_j])
                                        seen.add((n_i,n_j))
                                        visited.add((n_i,n_j))

                    max_area = max(max_area, area)    
        
        return max_area





        