from collections import deque

# initilaizing the capacity of each jug in a tuple 
capacity = (8, 5, 3)

# using BFS function to solve the problem
def solve_jugs():
    initial_position = (8, 0, 0)
    # making a queue for breadth first search
    queue = deque([initial_position])
    # tracking the visited positions
    visited = set([initial_position])
    
    # applying the Breadth first search 
    while queue:
        current_pos = queue.popleft()
        a, b, c = current_pos  # getting the current position of jugs

        # Check if we have reached our goal which is any 4 pint in a jug
        if a == 4 or b == 4 or c == 4:
            print(f"The puzzle is solved! The position with 4 pints is {current_pos}")
            return current_pos 
        
        # Exhausting the pourings between the jugs 
        for (jug_out, jug_in) in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]:
            # Creating a list from current_pos to modify pouring
            new_pos = list(current_pos)
            
            # Calculating the amount of water we can transfer from one jug to another 
            pour_amount = min(new_pos[jug_out], capacity[jug_in] - new_pos[jug_in])
            new_pos[jug_out] = new_pos[jug_out] - pour_amount
            new_pos[jug_in] = new_pos[jug_in] + pour_amount
            new_pos = tuple(new_pos)  # Converting the list back to tuple
            
            # If the new position is not visited we enqueue it
            if new_pos not in visited:
                visited.add(new_pos)
                queue.append(new_pos)
                print(f"Visited positions are {new_pos}")  
    
    
    print("No solution found.")
    return None


solve_jugs()
