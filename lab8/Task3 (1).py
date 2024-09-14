# Implement the 8 puzzle problem using a* search in python

import heapq

# Helper function to find the position of the empty space (0) in the puzzle
def find_zero_position(state):
    for i, row in enumerate(state):
        if 0 in row:
            return i, row.index(0)

# Heuristic function: Number of misplaced tiles
def misplaced_tiles(state, goal):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != 0 and state[i][j] != goal[i][j])

# Generate the neighbors of the current state
def generate_neighbors(state):
    neighbors = []
    x, y = find_zero_position(state)
    directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    
    for dx, dy in directions:
        if 0 <= dx < 3 and 0 <= dy < 3:
            # Copy the current state
            new_state = [row[:] for row in state]
            # Swap the empty space with the neighboring tile
            new_state[x][y], new_state[dx][dy] = new_state[dx][dy], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors

# A* Search function
def a_star_search(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (misplaced_tiles(start, goal), 0, start, []))
    
    visited = set()
    
    while priority_queue:
        _, cost, current_state, path = heapq.heappop(priority_queue)
        
        # Add the current state to the path
        path = path + [current_state]
        
        if current_state == goal:
            print("Goal reached!")
            print("Path:")
            for step in path:
                for row in step:
                    print(row)
                print()
            print(f"Total Moves: {cost}")
            return
        
        # Serialize state to make it hashable for the visited set
        state_tuple = tuple(tuple(row) for row in current_state)
        if state_tuple in visited:
            continue
        
        visited.add(state_tuple)
        
        # Explore neighbors
        for neighbor in generate_neighbors(current_state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                total_cost = cost + 1
                heapq.heappush(priority_queue, (total_cost + misplaced_tiles(neighbor, goal), total_cost, neighbor, path))

# Initial state (can be customized)
start_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

# Goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Start the search
a_star_search(start_state, goal_state)
