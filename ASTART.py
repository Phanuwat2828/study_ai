import heapq
import itertools

class Graph:
    def __init__(self, adjacent, heuristics):
        self.adjacent = adjacent
        self.heuristics = heuristics
    
    def get_neighbors(self, node):  # Fixed typo: get_heighbors -> get_neighbors
        return self.adjacent.get(node, [])

    def h(self, node):
        return self.heuristics.get(node, float('inf'))

class AStar:  # Fixed typo: Astart -> AStar
    def __init__(self, graph):
        self.graph = graph
        self.counter = itertools.count()

    def search(self, start, goal):
        # Priority queue: (f_cost, g_cost, counter, node)
        frontier = []
        heapq.heappush(
            frontier,
            (self.graph.h(start), 0, next(self.counter), start)
        )

        # Cost from start to node
        g_cost = {start: 0}
        # Parent tracking for path reconstruction
        parents = {start: None}
        # Visited set to avoid reprocessing
        visited = set()
        # Track order of expansion for visualization
        expansion_order = []

        print(f"{'='*50}")
        print(f"A* SEARCH")
        print(f"From: {start} → To: {goal}")
        print(f"{'='*50}\n")

        while frontier:
            # Get node with smallest f_cost
            f_current, g_current, _, current_node = heapq.heappop(frontier)
            
            print(f"Popped: {current_node} (f={f_current:.1f}, g={g_current:.1f}, h={self.graph.h(current_node):.1f})")
            
            # Check if we found the goal
            if current_node == goal:
                print(f"\n✓ Goal '{goal}' reached!")
                return self._reconstruct_path(parents, current_node), g_current

            # Skip if already processed
            if current_node in visited:
                print(f"  ↳ Already visited, skipping")
                continue

            # Mark as visited and record expansion order
            visited.add(current_node)
            expansion_order.append(current_node)
            print(f"  ✓ Expanded {current_node} (Order #{len(expansion_order)})")
            
            # Explore neighbors
            neighbors = self.graph.get_neighbors(current_node)
            if not neighbors:
                print(f"  ↳ No neighbors")
                continue
                
            print(f"  Neighbors: {neighbors}")
            
            for neighbor, weight in neighbors:
                if neighbor in visited:
                    print(f"    → {neighbor}: already visited, skipping")
                    continue
                
                # Calculate tentative g_cost
                tentative_g = g_current + weight
                
                # If this path is better than any previous one
                if tentative_g < g_cost.get(neighbor, float('inf')):
                    print(f"    → {neighbor}: updating path (g={tentative_g:.1f})")
                    # Update costs and parent
                    g_cost[neighbor] = tentative_g
                    parents[neighbor] = current_node
                    # Calculate f_cost = g_cost + heuristic
                    f_cost = tentative_g + self.graph.h(neighbor)
                    
                    # Add to frontier
                    heapq.heappush(
                        frontier,
                        (f_cost, tentative_g, next(self.counter), neighbor)
                    )
                    print(f"       Added to frontier with f={f_cost:.1f}, h={self.graph.h(neighbor):.1f}")
                else:
                    print(f"    → {neighbor}: existing path is better ({g_cost.get(neighbor, float('inf')):.1f} < {tentative_g:.1f})")

            print()  # Empty line for readability

        print("\n✗ Goal not reachable!")
        return None, float('inf')

    def _reconstruct_path(self, parents, current_node):
        """Reconstruct path from start to current_node"""
        path = []
        while current_node is not None:
            path.append(current_node)
            current_node = parents[current_node]
        return path[::-1]

# Graph data with weighted edges
Graph_data = {
    'S': [('A', 2), ('D', 5)],
    'A': [('B', 3), ('C', 4)],
    'D': [('B', 3), ('E', 4)],
    'B': [('C', 3), ('E', 5)],
    'E': [('G', 6)],
    'C': [('G', 2)],
}

# Heuristic values (estimated cost to goal 'G')
h_data = {
    'S': 7,
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'G': 0,
    'E': 3,
}

# Create graph and run A* search
graph = Graph(Graph_data, h_data)
astar = AStar(graph)
path, total_cost = astar.search('S', 'G')

# Print results
print(f"{'='*50}")
print("RESULTS")
print(f"{'='*50}")
if path:
    print(f"✓ Shortest path found: {' → '.join(path)}")
    print(f"✓ Total cost: {total_cost}")
    print(f"✓ Path length: {len(path) - 1} steps")
    
    # Calculate and verify path cost
    actual_cost = 0
    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i+1]
        for neighbor, weight in Graph_data.get(current, []):
            if neighbor == next_node:
                actual_cost += weight
                break
    print(f"✓ Verified cost: {actual_cost}")
else:
    print("✗ No path found to goal")

print(f"{'='*50}")

# Optional: Test with different start points
print("\n\nTesting additional scenarios:")
print(f"{'='*50}")

test_cases = [
    ('S', 'G'),
    ('A', 'G'),
    ('D', 'G'),
    ('B', 'G'),
]

for start, goal in test_cases:
    path, cost = astar.search(start, goal)
    if path:
        print(f"From {start} to {goal}: {' → '.join(path)} (cost: {cost})")
    else:
        print(f"From {start} to {goal}: No path found")