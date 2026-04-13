import heapq

def a_star(grid, start, goal):
    """
    A* path planning algorithm.
    Returns the path from start to goal as a list of positions.
    """
    rows, cols = grid.shape
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + di, current[1] + dj)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor] == 0:
                new_cost = cost_so_far[current] + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristic(goal, neighbor)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

    # Reconstruct path
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from.get(current)
        if current is None:
            return []  # No path
    path.reverse()
    return path