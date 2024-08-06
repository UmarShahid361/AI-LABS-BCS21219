# Task 1

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, node, neighbour):
        if node not in self.adj:
            self.adj[node] = set()

        if neighbour not in self.adj:
            self.adj[neighbour] = set()
        self.adj[node].add(neighbour)
        self.adj[neighbour].add(node)

    def dfs(self, start, target):
        stack = Stack()
        visited = set()

        stack.push(start)
        visited.add(start)

        while not stack.is_empty():
            node = stack.pop()
            print(node, end=" ")

            if node == target:
                print("\nFound target")
                return

            for neighbour in self.adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.push(neighbour)

        print("\nTarget not found")
        return

dataGraph = {
    '1':{'2','7','8'},
    '2':{'3','6'},
    '3':{'4','5'},
    '4':{},
    '5':{},
    '6':{},
    '7':{},
    '8':{'9','12'},
    '9':{'10','11'},
    '10':{},
    '11':{},
    '12':{}
}

graph = Graph()
for node, neighbours in dataGraph.items():
    for neighbour in neighbours:
        graph.add_edge(node, neighbour)

graph.dfs('5', '11')



# Task 2

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, node, neighbour):
        if node not in self.adj:
            self.adj[node] = set()

        if neighbour not in self.adj:
            self.adj[neighbour] = set()
        self.adj[node].add(neighbour)
        self.adj[neighbour].add(node)

    def dfs(self, start, target):
        stack = Stack()
        visited = set()

        stack.push(start)
        visited.add(start)

        while not stack.is_empty():
            node = stack.pop()
            print(node, end=" ")

            if node == target:
                print("\nFound target")
                return

            for neighbour in self.adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.push(neighbour)

        print("\nTarget not found")
        return

dataGraph = {
    'A': {'B', 'F','D','E'},
    'B': {'K', 'J'},
    'C': {},
    'D': {'G'},
    'E': {'C','H','I'},
    'F': {},
    'G': {},
    'H': {},
    'I': {'L'},
    'J': {},
    'K': {'N','M'},
    'L': {},
    'M': {},
    'N': {}
}

graph = Graph()
for node, neighbours in dataGraph.items():
    for neighbour in neighbours:
        graph.add_edge(node, neighbour)

graph.dfs('A', 'G')