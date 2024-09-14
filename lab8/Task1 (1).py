# implement greedy best first search in python
import heapq

# Define the Romania map graph with straight-line distances (heuristics) to Bucharest
romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Oradea': [('Sibiu', 151), ('Zerind', 71)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Arad', 140), ('Oradea', 151)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia': [('Drobeta', 75), ('Lugoj', 70)],
    'Drobeta': [('Craiova', 120), ('Mehadia', 75)],
    'Craiova': [('Pitesti', 138), ('Drobeta', 120), ('Rimnicu Vilcea', 146)],
    'Rimnicu Vilcea': [('Pitesti', 97), ('Sibiu', 80), ('Craiova', 146)],
    'Fagaras': [('Bucharest', 211), ('Sibiu', 99)],
    'Pitesti': [('Bucharest', 101), ('Rimnicu Vilcea', 97), ('Craiova', 138)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90)],
    'Giurgiu': [('Bucharest', 90)],
}

# Heuristic: Straight-line distances to Bucharest
heuristics = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0,
    'Giurgiu': 77,
}

def greedy_best_first_search(start, goal):
    # Priority queue with heuristic as priority
    priority_queue = []
    heapq.heappush(priority_queue, (heuristics[start], start))
    
    visited = set()
    
    while priority_queue:
        # Get the node with the lowest heuristic value
        _, current_node = heapq.heappop(priority_queue)
        
        print(f"Visiting: {current_node}")
        
        if current_node == goal:
            print("Goal reached!")
            return
        
        visited.add(current_node)
        
        # Explore neighbors
        for neighbor, _ in romania_map[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))

# Start the search
greedy_best_first_search('Arad', 'Bucharest')
