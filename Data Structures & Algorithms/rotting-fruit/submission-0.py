from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
        #UMPIRE : Understand Match Plan Implement Review Evaluate
        # I can look at the question from another perspective, remembering that the 
        # BFS expand itself in bubbles of the same distance from the source. I can ask
        # What is the longest buble that the algorithm from any of the rotten bananas has 
        # to perform to reach the farthest fruit?
        # I can scan the matrix in search for valid starting rotten fruites.
        # The thing is that they may happen to work together to reach before the solution
        # so i cannot consider them to work independently.

        # I can immagine to simulate in parallel step of BFS from different sources.
        # I can insert all the rotten banana position in the same stack and then run a bfs
        # step and count how many step i need to do before reaching the full rott.
        # While scanning for starting point i can also write the position of each 
        # fruit so in the end i can check if all are visited otherwise
        # it's not reachable
        offsets = [[0,-1], [-1,0],[0,1],[1,0]]
        starting_fresh_fruit = set() #[i,j]
        seen = set()
        initial_queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    starting_fresh_fruit.add((row,col))
                elif grid[row][col] == 2:
                    initial_queue.append((row,col))
                    seen.add((row,col))

        swap_queue = deque()
        # Now i can simulate steps of the BFS algorithm

        count = 0
        print(initial_queue, seen, starting_fresh_fruit)
        while True:
            visiting_i, visiting_j = initial_queue.popleft()
            print(visiting_i, visiting_j)
            # Now i need to visit the neighbors and add them only
            # if they are rotten fruit and not already visited
            # and remember to remove them from rotten fruit
            for offset in offsets:
                n_i = visiting_i + offset[0]
                n_j = visiting_j + offset[1]

                if 0<=n_i < len(grid) and 0<= n_j < len(grid[0]):
                    if grid[n_i][n_j] == 1 and(n_i,n_j) not in seen:
                        #now it's rotten
                        starting_fresh_fruit.remove((n_i,n_j))
                        seen.add((n_i,n_j))

                        #It's going to be processed in the next step
                        swap_queue.append((n_i,n_j))


            
            if not initial_queue:
                if not swap_queue:
                    break
                count+=1
                initial_queue = swap_queue
                swap_queue = deque()

        
        # Check if there's still unreached fruit, otherwise return steps
        if starting_fresh_fruit :
            return -1
        
        return count
            












        