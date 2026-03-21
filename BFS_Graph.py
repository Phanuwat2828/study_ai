

#66011212124 Phanuwat Khamtha
from collections import deque
import time 

graph = {
    'S': ['A', 'B','C'],
    'B': ['F','G'],
    'A': ['D', 'E'],
    'C': ['H'],
    'H': ['I', 'J'],
    'I': ['M', 'L', 'K'],
    'D': [],  # Add empty lists for leaf nodes
    'E': [],
    'F': [],
    'G': [],
    'J': [],
    'M': [],
    'L': [],
    'K': []
}

def bfs_graph_search(graph, start, goal):
    if start not in graph:
        print("Start node not in graph")
        return False
    queue = deque([start])
    visited = {start}
    print(f"Starting BFS from {start} to find {goal}")
    while queue:
        print("queue: ", queue)
        current = queue.popleft()
        print("processing: ", current)  # Changed from "visited: "
        if current == goal:
            print(f"Goal {goal} found!")
            return True
        if current in graph:  # Check if node has neighbors
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        time.sleep(0.5)
    return False

#66011212124 Phanuwat Khamtha
def solution(start, goal):
    found = bfs_graph_search(graph, start, goal)
    if found:
        sol = "Solution found!" + goal
    else:
        sol = "No solution found." + goal
    print(sol)
    
solution('S', 'I')