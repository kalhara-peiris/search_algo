# Task 3: Develop a function to calculate the heuristic cost using Chebyshev Distance

def chebyshev_distance(node, goal):
    """
    Calculate the Chebyshev distance between two points.
    
    Chebyshev distance is defined as: d(N, G) = max(|Nx - Gx|, |Ny - Gy|)
    where (Nx, Ny) is the current node and (Gx, Gy) is the goal node.
    
    Args:
        node: Tuple (x, y) representing current node coordinates
        goal: Tuple (x, y) representing goal node coordinates
        
    Returns:
        The Chebyshev distance value
    """
    nx, ny = node
    gx, gy = goal
    
    # Chebyshev distance formula: max(|Nx - Gx|, |Ny - Gy|)
    return max(abs(nx - gx), abs(ny - gy))

# If this file is run directly, demonstrate the heuristic calculation
if __name__ == "__main__":
    # Example nodes for testing
    test_nodes = [
        ((0, 0), (5, 5)),  # Corner to corner
        ((2, 2), (4, 4)),  # Center to off-center
        ((1, 3), (5, 3)),  # Same row
        ((3, 1), (3, 5)),  # Same column
        ((2, 3), (3, 4))   # Diagonal neighbors
    ]
    
    print("Chebyshev Distance Heuristic Examples:")
    print("-------------------------------------")
    for node, goal in test_nodes:
        distance = chebyshev_distance(node, goal)
        print(f"Node {node} to Goal {goal}: {distance}")
        
    # Explanation
    print("\nExplanation:")
    print("The Chebyshev distance represents the minimum number of moves")
    print("needed to reach the goal in a grid where diagonal moves are allowed.")
    print("It's an admissible heuristic for A* search in this maze problem.")