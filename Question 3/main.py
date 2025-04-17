"""
Main script to run all tasks for Question 3: Maze Search Algorithms
"""

def main():
    print("Running task5.py to execute all experiments and analysis...")
    print("This will demonstrate all tasks 1-5 for Question 3.\n")
    
    # Import and run the task5 module which uses all other tasks
    from task5 import run_experiments
    run_experiments(3)  # Run experiments on 3 random mazes
    
    print("\nAll tasks completed successfully!")

if __name__ == "__main__":
    main()