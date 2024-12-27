import heapq


class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """

        '''
        need to track steps, obstacles-remaining, (x,y),
        if we want to get the shortest path, by eliminating k obstacles, 
            order the entry in pq by number of steps first
        '''
        rows = len(grid)
        cols = len(grid[0])
        min_steps = [[float('inf')] * cols for _ in range(rows)]
        min_steps[0][0] = 0

        # initial element in pq, to start of bfs search
        pq = [(0, k, 0, 0)]  # steps, obstacles-remaining, x, y

        x_limit = rows - 1
        y_limit = cols - 1
        while pq:
            steps, obstacles_remaining, r, c = heapq.heappop(pq)

            next_steps = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in next_steps:

                if nr > x_limit or nr < 0 or nc > y_limit or nc < 0:
                    continue

                if nr == x_limit and nc == y_limit:
                    print("reached end state")
                    return steps+1

                n_obstacles_remaining = obstacles_remaining - grid[nr][nc]

                # we cannot go in debt to remove obstacles
                if n_obstacles_remaining < 0:
                    continue

                n_steps = steps + 1

                """
                BIG ISSUE WITH THIS CODE:
                    NOT OPTIMIZING FOR REMAINING OBSTACLES COUNT, 
                    IF WE REACH A GRID LOCATION WITH GREATER OBSTACLE COUNT THEN PREVIOUSLY, WE IGNORE IT,
                    WE ARE ONLY UPDATING MIN_STEPS DP ARRAY IF THE STEPS TO REACH CURRENT CELL IS LESSER, 
                    IS OBSTACLES REMAINING WERE MORE, THIS COULD EVENTUALLY CAUSE A MORE OPTIMAL RESULT 
                """
                if steps < min_steps[nr][nc]:
                    min_steps[nr][nc] = n_steps
                    heapq.heappush(pq, (n_steps, n_obstacles_remaining, nr, nc))

        if min_steps[x_limit][y_limit] == float("inf"):
            return -1
        return min_steps[x_limit][y_limit]
object = Solution()
# grid = [
#         [0, 0, 0],
#         [1, 1, 1],
#         [0, 0, 1],
#         [1, 1, 1],
#         [0, 0, 0]
# ]
# grid = [
#         [0, 0, 0],
#         [1, 1, 0],
#         [0, 0, 0],
#         [0, 1, 1],
#         [0, 0, 0],
# ]


# grid = [[0]]

grid = [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]]

k = 1
# k = 5
print(object.shortestPath(grid, k))
