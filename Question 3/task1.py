import random

# Task 1
def setup_maze():
    # Initialize empty maze (6x6)
    maze = [[0 for _ in range(6)] for _ in range(6)]
    
    # Randomly select starting node (0-11)
    possible_start_nodes = []
    for i in range(2):  # First two rows (0-1)
        for j in range(6):  # All columns (0-5)
            possible_start_nodes.append((i, j))
    
    start_pos = random.choice(possible_start_nodes)
    start_row, start_col = start_pos
    maze[start_row][start_col] = 'S' 
    
    # Randomly select goal node (24-35)
    possible_goal_nodes = []
    for i in range(4, 6):  
        for j in range(6):  
            possible_goal_nodes.append((i, j))
    
    goal_pos = random.choice(possible_goal_nodes)
    goal_row, goal_col = goal_pos
    maze[goal_row][goal_col] = 'G'  # 'G' for goal
    
    # Randomly select 4 barrier nodes
    barrier_count = 0
    while barrier_count < 4:
        barrier_row = random.randint(0, 5)
        barrier_col = random.randint(0, 5)
        if maze[barrier_row][barrier_col] == 0:  # Only select empty cells
            maze[barrier_row][barrier_col] = 'B'  # 'B' for barrier
            barrier_count += 1
            
    return maze, start_row, start_col, goal_row, goal_col

# Helper function to convert node coordinates to node number (0-35)
def coordinates_to_node_number(row, col):
    return row * 6 + col

# Helper function to display the maze
def display_maze(maze, path=None):
    maze_display = [row[:] for row in maze]  # Create a copy
    
    # Mark path on the maze copy
    if path:
        for r, c in path:
            if maze_display[r][c] != 'S' and maze_display[r][c] != 'G':
                maze_display[r][c] = 'P'  # 'P' for path
    
    # Print the maze
    for row in maze_display:
        for cell in row:
            if cell == 0:
                print("00", end=" ")
            elif cell == 'S':
                print("ST", end=" ")
            elif cell == 'G':
                print("GO", end=" ")
            elif cell == 'B':
                print("BA", end=" ")
            elif cell == 'P':
                print("PA", end=" ")
        print()

# If this file is run directly, demonstrate maze setup
if __name__ == "__main__":
    maze, start_row, start_col, goal_row, goal_col = setup_maze()
    print(f"Start: ({start_row}, {start_col}) = Node {coordinates_to_node_number(start_row, start_col)}")
    print(f"Goal: ({goal_row}, {goal_col}) = Node {coordinates_to_node_number(goal_row, goal_col)}")
    print("\nGenerated Maze:")
    display_maze(maze)