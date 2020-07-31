class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        '''def get_coordinates(x, y, max_x, max_y): 
            coordinates = []
            pos_x = x + 1 
            pos_y = y + 1 
            neg_x = x - 1 
            neg_y = y - 1
            if pos_x < max_x: 
                coordinates.append((pos_x, y))
            if pos_y < max_y: 
                coordinates.append((x, pos_y))
            if neg_x >= 0: 
                coordinates.append((neg_x, y))
            if neg_y >= 0: 
                coordinates.append((x, neg_y))
            return coordinates
        
        #Base cases
        if len(grid) == 0: 
            return 0 
        if len(grid[0]) == 0: 
            return 0 
        #use bfs to find the first 1, bfs the 1's to set all to 0, add those to visited set, continue to bfs until all done 
        visited = {}#dictionary for O(1) lookup 
        max_i = len(grid)
        max_j = len(grid[0])
        num_islands = 0
        for i in range(0, max_i): 
            for j in range(0, max_j): 
                if grid[i][j] == '1':
                    num_islands += 1
                    queue = [(i, j)]
                    while (len(queue) != 0): 
                        #print(len(queue))
                        (cur_i, cur_j) = queue.pop(0)
                        grid[cur_i][cur_j] = '0'
                        if ((cur_i + 1 < max_i) and (grid[cur_i + 1][cur_j] == '1')):
                            #print((cur_i + 1, cur_j) in queue == False)
                            if (((cur_i + 1, cur_j) in queue) == False): 
                                queue.append((cur_i + 1, cur_j))
                        if ((cur_j + 1 < max_j) and (grid[cur_i][cur_j + 1] == '1')): 
                            if (((cur_i, cur_j + 1) in queue) == False):
                                queue.append((cur_i, cur_j + 1))
                        if ((cur_i - 1 >= 0) and (grid[cur_i - 1][cur_j] == '1')): 
                            if (((cur_i - 1, cur_j) in queue) == False):
                                queue.append((cur_i - 1, cur_j))
                        if ((cur_j - 1 >= 0) and (grid[cur_i][cur_j-1] == '1')): 
                            if (((cur_i, cur_j - 1) in queue) == False):
                                queue.append((cur_i, cur_j - 1))
                            
        
        return num_islands'''
        #base case:
        if len(grid) == 0:
            return 0 #null map
        
        def findNeighbors(i, j):
            return (i+1, j), (i-1, j), (i, j+1), (i, j-1)
        
        max_x = len(grid)
        max_y = len(grid[0])
        num_islands = 0
        land = {}
        seen_land = {}
        for i in range(0, max_x):
            for j in range(0, max_y):
                if grid[i][j] == '1':
                    land[(i, j)] = True
        #backward pass 
        #print(((0, 0) in seen_land))
        for l in land.keys():
            #print(l)
            if (l in seen_land) == False: #land not seen before
                #print(l)
                seen_land[l] = True
                num_islands += 1
                stack = [l]
                while len(stack) != 0: #BFS to add all lands to seen lands
                    node = stack.pop(0)
                    (i, j) = node
                    #seen_land[node] = True
                    n1, n2, n3, n4 = findNeighbors(i, j)
                    if (((n1 in seen_land) == False) and (n1 in land)):
                        seen_land[n1] = True
                        stack.append(n1)
                    if (((n2 in seen_land) == False) and (n2 in land)):
                        seen_land[n2] = True
                        stack.append(n2)
                    if (((n3 in seen_land) == False) and (n3 in land)):
                        seen_land[n3] = True
                        stack.append(n3)
                    if (((n4 in seen_land) == False) and (n4 in land)):
                        seen_land[n4] = True
                        stack.append(n4)
        return num_islands
        
