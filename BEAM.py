from collections import deque

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': ['K'],
    'G': [],
    'H': ['C'],
    'I': [],
    'J': ['L'],
    'K': []
}

# Heuristic function (estimate distance to goal)
# Smaller value = closer to goal
def heuristic(node, goal='J'):
    # Simple heuristic based on alphabetical distance
    # You can customize this based on your problem
    if node == goal:
        return 0
    
    # Example: Manhattan distance in alphabetical order
    # This is just a demonstration - adjust for your actual problem
    goal_index = ord(goal) - ord('A')
    node_index = ord(node) - ord('A') if 'A' <= node <= 'Z' else 999
    
    # Predefined heuristic values for better demonstration
    heuristics = {
        'A': 4, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
        'F': 4, 'G': 4, 'H': 3, 'I': 4, 'J': 0,
        'K': 5, 'L': 1
    }
    
    return heuristics.get(node, 10)

# Expand function - returns neighbors of a node
def expand(node):
    return graph.get(node, [])

def extract_path(parent, goal):
    """Extract the path from start to goal using parent dictionary"""
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)  # Use .get() to avoid KeyError
    return path[::-1]

def beam_search(start_node, goal_state, beam_width, max_iterations=100):
    """
    Beam Search Algorithm
    
    Args:
        start_node: Starting node
        goal_state: Target node
        beam_width: Number of nodes to keep at each level
        max_iterations: Maximum iterations to prevent infinite loops
    
    Returns:
        Path from start to goal if found, None otherwise
    """
    print(f"\n{'='*60}")
    print(f"BEAM SEARCH")
    print(f"Start: {start_node}, Goal: {goal_state}, Beam Width: {beam_width}")
    print(f"{'='*60}")
    
    # frontier = nodes currently being considered
    frontier = [start_node]
    visited = set()
    
    # Store parent relationships for path reconstruction
    parent = {start_node: None}
    
    iteration = 0
    
    while frontier and iteration < max_iterations:
        iteration += 1
        
        print(f"\n{'─'*50}")
        print(f"Iteration {iteration} - Current Frontier: {frontier}")
        
        # Check if goal is in current frontier
        for node in frontier:
            if node == goal_state:
                print(f"\n✓ Goal '{goal_state}' found in current frontier!")
                return extract_path(parent, node)
        
        new_frontier = []
        
        # Expand every node in current beam
        for node in frontier:
            visited.add(node)
            
            children = expand(node)
            if children:
                print(f"  Expanding '{node}' → {children}")
            else:
                print(f"  Expanding '{node}' → (no children)")
            
            for child in children:
                # Prevent cycles
                if child not in visited:
                    # Record parent if not already recorded
                    if child not in parent:
                        parent[child] = node
                    new_frontier.append(child)
        
        if not new_frontier:
            print("\n✗ No more nodes to explore - search failed")
            return None
        
        # Remove duplicates while preserving order
        new_frontier = list(dict.fromkeys(new_frontier))
        
        # Sort by heuristic value (lower is better)
        new_frontier.sort(key=lambda n: heuristic(n, goal_state))
        
        # Show heuristic values
        print(f"  All candidates: {[(n, heuristic(n, goal_state)) for n in new_frontier]}")
        
        # Keep only the best beam_width nodes
        frontier = new_frontier[:beam_width]
        print(f"  Selected for next beam: {[(n, heuristic(n, goal_state)) for n in frontier]}")
        
        # Check if we've visited all nodes
        if all(node in visited for node in frontier):
            print("\n✗ All remaining nodes already visited - search failed")
            return None
    
    if iteration >= max_iterations:
        print(f"\n✗ Max iterations ({max_iterations}) reached")
    
    return None

def beam_search_with_trace(start_node, goal_state, beam_width):
    """
    Enhanced beam search that shows more detailed trace information
    """
    print(f"\n{'='*70}")
    print(f"BEAM SEARCH TRACE")
    print(f"Start: {start_node}, Goal: {goal_state}, Beam Width: {beam_width}")
    print(f"{'='*70}")
    
    frontier = [start_node]
    visited = set()
    parent = {start_node: None}
    level = 0
    
    while frontier:
        level += 1
        print(f"\n{'▬'*70}")
        print(f"LEVEL {level}")
        print(f"Current Beam (size {len(frontier)}): {frontier}")
        
        # Check goal
        for node in frontier:
            if node == goal_state:
                print(f"\n{'★'*70}")
                print(f"SUCCESS: Goal '{goal_state}' found at level {level}!")
                path = extract_path(parent, node)
                print(f"Path: {' → '.join(path)}")
                print(f"{'★'*70}")
                return path
        
        # Generate candidates
        candidates = []
        for node in frontier:
            visited.add(node)
            for child in expand(node):
                if child not in visited and child not in candidates:
                    if child not in parent:
                        parent[child] = node
                    candidates.append(child)
        
        if not candidates:
            print("\n✗ No more candidates to explore - search terminated")
            return None
        
        # Calculate heuristics
        candidates_with_h = [(c, heuristic(c, goal_state)) for c in candidates]
        candidates_with_h.sort(key=lambda x: x[1])
        
        print(f"Candidates (heuristic value): {candidates_with_h}")
        
        # Select best beam_width
        frontier = [c[0] for c in candidates_with_h[:beam_width]]
        
        if all(node in visited for node in frontier):
            print("\n✗ All selected nodes already visited - search failed")
            return None
    
    return None

# Test the implementations
print("\n" + "="*70)
print("TESTING BEAM SEARCH")
print("="*70)

# Test with different beam widths
test_cases = [
    ('A', 'J', 1, "Narrow beam (greedy)"),
    ('A', 'J', 2, "Medium beam"),
    ('A', 'J', 3, "Wide beam")
]

for start, goal, width, description in test_cases:
    print(f"\n{'█'*70}")
    print(f"TEST CASE: {description}")
    print(f"{'█'*70}")
    
    result = beam_search(start, goal, width)
    
    if result:
        print(f"\n{'✓'*70}")
        print(f"PATH FOUND (beam width={width}): {' → '.join(result)}")
        print(f"Path length: {len(result) - 1} steps")
        print(f"{'✓'*70}")
    else:
        print(f"\n{'✗'*70}")
        print(f"NO PATH FOUND with beam width={width}")
        print(f"{'✗'*70}")

# Run detailed trace for one case
print(f"\n{'█'*70}")
print("DETAILED TRACE EXAMPLE (Beam Width = 2)")
print(f"{'█'*70}")

detailed_result = beam_search_with_trace('A', 'J', 2)

if detailed_result:
    print(f"\n{'='*70}")
    print(f"FINAL RESULT: {' → '.join(detailed_result)}")
    print(f"{'='*70}")