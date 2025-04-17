import heapq
import math
from task3 import chebyshev_distance

# Helper function to calculate the edge cost between nodes
def calculate_cost(curr, neighbor):
    r1, c1 = curr
    r2, c2 = neighbor
    if r1 == r2 or c1 == c2:  # Horizontal or Vertical move
        return 1.0
    return math.sqrt(2)  # Diagonal move costs more

# Helper function to get valid neighbors (in increasing order of node number)
def get_neighbors(row, col):
    neighbors = [
        (row-1, col-1), (row-1, col), (row-1, col+1),  # Top row
        (row, col-1),               (row, col+1),      # Middle row (excluding current)
        (row+1, col-1), (row+1, col), (row+1, col+1)   # Bottom row
    ]
    valid_neighbors = []
    for r, c in neighbors:
        if 0 <= r < 6 and 0 <= c < 6:  # Check if within maze bounds
            valid_neighbors.append((r, c))
    
    # Sort by node number: node_number = row * 6 + col
    return sorted(valid_neighbors, key=lambda pos: pos[0] * 6 + pos[1])

# Task 4: A* Search using the Chebyshev Distance heuristic
def a_star_search(maze, start_row, start_col, goal_row, goal_col):
    # Priority queue for A*, initialized with start node
    # Format: (f_score, (row, col)) where f_score = g_score + heuristic
    start_f_score = chebyshev_distance((start_row, start_col), (goal_row, goal_col))
    pq = [(start_f_score, (start_row, start_col))]
    
    visited = set()  # Set to track visited nodes
    came_from = {}  # For path reconstruction
    g_score = {(start_row, start_col): 0}  # Cost from start to node
    f_score = {(start_row, start_col): start_f_score}  # Estimated total cost
    visited_nodes = []  # To track all visited nodes in order
    total_time = 0  # Total time to reach the goal (1 minute per node)

    while pq:
        # Get the node with the lowest f_score
        _, (row, col) = heapq.heappop(pq)
        
        # If we've already processed this node, skip it
        if (row, col) in visited:
            continue
        
        # Mark the node as visited and update visited nodes
        visited.add((row, col))
        visited_nodes.append((row, col))
        total_time += 1  # Each node takes 1 minute to explore
        
        # If goal is found, reconstruct the path
        if (row, col) == (goal_row, goal_col):
            path = []
            current = (row, col)
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append((start_row, start_col))
            path.reverse()  # Reverse the path to get from start to goal
            return visited_nodes, total_time, path
        
        # Explore neighbors
        for neighbor in get_neighbors(row, col):
            nr, nc = neighbor
            if maze[nr][nc] != 'B' and (nr, nc) not in visited:  # Skip barriers and visited nodes
                move_cost = calculate_cost((row, col), neighbor)
                tentative_g_score = g_score[(row, col)] + move_cost
                
                if (nr, nc) not in g_score or tentative_g_score < g_score[(nr, nc)]:
                    # This path to neighbor is better than any previous one
                    came_from[(nr, nc)] = (row, col)
                    g_score[(nr, nc)] = tentative_g_score
                    f_score_val = tentative_g_score + chebyshev_distance((nr, nc), (goal_row, goal_col))
                    f_score[(nr, nc)] = f_score_val
                    heapq.heappush(pq, (f_score_val, (nr, nc)))
        
    return visited_nodes, total_time, []  # In case no path is found

# If this file is run directly, test A* on a sample maze
if __name__ == "__main__":
    from task1 import setup_maze, display_maze, coordinates_to_node_number
    
    maze, start_row, start_col, goal_row, goal_col = setup_maze()
    print(f"Start: ({start_row}, {start_col}) = Node {coordinates_to_node_number(start_row, start_col)}")
    print(f"Goal: ({goal_row}, {goal_col}) = Node {coordinates_to_node_number(goal_row, goal_col)}")
    print("\nInitial Maze:")
    display_maze(maze)
    
    visited_nodes, time_taken, path = a_star_search(maze, start_row, start_col, goal_row, goal_col)
    
    print("\nA* Search Results:")
    print(f"Visited Nodes: {[coordinates_to_node_number(r, c) for r, c in visited_nodes]}")
    print(f"Time Taken: {time_taken} minutes")
    print(f"Path Found: {[coordinates_to_node_number(r, c) for r, c in path]}")
    print(f"Path Length: {len(path)}")
    
    print("\nA* Path on Maze:")
    display_maze(maze, path)