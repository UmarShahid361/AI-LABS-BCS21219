import networkx as nx
import matplotlib.pyplot as plt

graph = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 3]
}

G = nx.Graph()

for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15, font_weight='bold')

plt.title("Graph Visualization")
plt.show()




from collections import deque

def bfs_find_target(graph, start, target):
    explored = set()
    frontier = deque([start])
    
    while frontier:
        node = frontier.popleft()
        print(f"Visiting {node}")
        
        if node == target:
            print(f"Found target {target}")
            return True
        
        explored.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in explored:
                frontier.append(neighbor)
    
    print(f"Target {target} not found")
    return False

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': ['D'],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': [],
}

# Starting BFS from vertex 'A' to find 'L'
print("BFS traversal to find 'L' starting from vertex 'A':")
bfs_find_target(graph, 'A', 'G')



import heapq

class PriorityQueue:
    def _init_(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


pq = PriorityQueue()

pq.put("task1", 3)
pq.put("task2", 1)
pq.put("task3", 2)

while not pq.is_empty():
    task = pq.get()
    print(task)