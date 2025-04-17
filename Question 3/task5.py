import numpy as np
from task1 import setup_maze, display_maze, coordinates_to_node_number
from task2 import uniform_cost_search
from task4 import a_star_search

# Task 5: Run experiments with both search algorithms on 3 different random mazes

def run_experiments(num_mazes=3):
    """
    Run both UCS and A* search on multiple random mazes and analyze the results.
    
    Args:
        num_mazes: Number of random mazes to generate and test (default: 3)
    """
    # Arrays to store results for statistical analysis
    ucs_times = []
    ucs_path_lengths = []
    astar_times = []
    astar_path_lengths = []
    
    # Run experiments on multiple mazes
    for i in range(num_mazes):
        print(f"\n{'='*50}")
        print(f"MAZE {i+1}")
        print(f"{'='*50}")
        
        # Generate random maze
        maze, start_row, start_col, goal_row, goal_col = setup_maze()
        
        print(f"Start: ({start_row}, {start_col}) = Node {coordinates_to_node_number(start_row, start_col)}")
        print(f"Goal: ({goal_row}, {goal_col}) = Node {coordinates_to_node_number(goal_row, goal_col)}")
        print("\nInitial Maze:")
        display_maze(maze)
        
        # Run Uniform Cost Search
        print("\nRunning Uniform Cost Search...")
        ucs_visited, ucs_time, ucs_path = uniform_cost_search(maze, start_row, start_col, goal_row, goal_col)
        
        if ucs_path:  # If path was found
            print(f"UCS Visited Nodes: {[coordinates_to_node_number(r, c) for r, c in ucs_visited]}")
            print(f"UCS Time: {ucs_time} minutes")
            print(f"UCS Path: {[coordinates_to_node_number(r, c) for r, c in ucs_path]}")
            print(f"UCS Path Length: {len(ucs_path)}")
            print("\nUCS Path on Maze:")
            display_maze(maze, ucs_path)
            
            # Store results
            ucs_times.append(ucs_time)
            ucs_path_lengths.append(len(ucs_path))
        else:
            print("UCS could not find a path!")
        
        # Run A* Search
        print("\nRunning A* Search...")
        astar_visited, astar_time, astar_path = a_star_search(maze, start_row, start_col, goal_row, goal_col)
        
        if astar_path:  # If path was found
            print(f"A* Visited Nodes: {[coordinates_to_node_number(r, c) for r, c in astar_visited]}")
            print(f"A* Time: {astar_time} minutes")
            print(f"A* Path: {[coordinates_to_node_number(r, c) for r, c in astar_path]}")
            print(f"A* Path Length: {len(astar_path)}")
            print("\nA* Path on Maze:")
            display_maze(maze, astar_path)
            
            # Store results
            astar_times.append(astar_time)
            astar_path_lengths.append(len(astar_path))
        else:
            print("A* could not find a path!")
    
    # Statistical Analysis
    print(f"\n{'='*50}")
    print("STATISTICAL ANALYSIS")
    print(f"{'='*50}")
    
    if ucs_times and astar_times:
        # Mean and variance of solution times
        print("\nSolution Times:")
        print(f"UCS Mean Time: {np.mean(ucs_times):.2f} minutes")
        print(f"UCS Time Variance: {np.var(ucs_times):.2f}")
        print(f"A* Mean Time: {np.mean(astar_times):.2f} minutes")
        print(f"A* Time Variance: {np.var(astar_times):.2f}")
        
        # Mean and variance of path lengths
        print("\nPath Lengths:")
        print(f"UCS Mean Path Length: {np.mean(ucs_path_lengths):.2f}")
        print(f"UCS Path Length Variance: {np.var(ucs_path_lengths):.2f}")
        print(f"A* Mean Path Length: {np.mean(astar_path_lengths):.2f}")
        print(f"A* Path Length Variance: {np.var(astar_path_lengths):.2f}")
    
    # Algorithm Analysis
    print(f"\n{'='*50}")
    print("ALGORITHM COMPARISON")
    print(f"{'='*50}")
    
    print("\n1. Completeness Analysis:")
    print("   - Both UCS and A* are complete algorithms in finite search spaces.")
    print("   - They will always find a solution if one exists, as demonstrated in our experiments.")
    print("   - Both algorithms systematically explore the search space until a goal is reached.")
    
    print("\n2. Optimality Analysis:")
    print("   - UCS guarantees optimality by always expanding the node with the lowest path cost.")
    print("   - A* guarantees optimality when using an admissible heuristic like Chebyshev distance.")
    if ucs_path_lengths and astar_path_lengths:
        if np.mean(ucs_path_lengths) == np.mean(astar_path_lengths):
            print("   - In our experiments, both algorithms found paths of the same length, confirming optimality.")
        else:
            print("   - Path length differences observed may be due to equal-cost paths or implementation details.")
    
    print("\n3. Time Complexity Analysis:")
    print("   - UCS has a time complexity of O(b^(1 + C/ε)) where:")
    print("     - b is the branching factor (maximum up to 8 in our maze)")
    print("     - C is the cost of the optimal solution")
    print("     - ε is the minimum edge cost (1 in our maze)")
    print("   - A* has a worst-case time complexity of O(b^d) where d is the solution depth")
    print("   - However, with a good heuristic, A* typically performs much better in practice")
    
    if ucs_times and astar_times:
        ucs_mean = np.mean(ucs_times)
        astar_mean = np.mean(astar_times)
        if astar_mean < ucs_mean:
            print(f"   - In our experiments, A* explored fewer nodes on average ({astar_mean:.2f}) compared to UCS ({ucs_mean:.2f})")
            print(f"   - This represents a {((ucs_mean - astar_mean) / ucs_mean * 100):.2f}% reduction in nodes explored")
            print("   - This demonstrates the efficiency advantage of using the Chebyshev distance heuristic")
        elif astar_mean == ucs_mean:
            print(f"   - In our experiments, both algorithms explored the same number of nodes on average ({astar_mean:.2f})")
            print("   - This could happen in simple mazes or when the heuristic provides limited guidance")
        else:
            print(f"   - In our experiments, UCS explored fewer nodes on average ({ucs_mean:.2f}) compared to A* ({astar_mean:.2f})")
            print("   - This is unusual and might be due to the specific maze configurations or implementation details")
    
    print("\nConclusion:")
    print("While both algorithms are complete and optimal, A* typically explores fewer nodes than UCS")
    print("due to its use of the heuristic function to guide the search toward the goal.")
    print("This makes A* more efficient for pathfinding problems like our maze navigation task.")

# If this file is run directly, run the experiments
if __name__ == "__main__":
    run_experiments(3)  # Run on 3 random mazes